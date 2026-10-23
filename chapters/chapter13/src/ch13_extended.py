"""Chapter 13 §§13.3, 13.6, 13.8: manuscript-aligned reconstructed executable examples."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import platform
import sys
import numpy as np
import pandas as pd
import scipy
from scipy.optimize import least_squares, curve_fit
from ch13_examples import concentration_model, sha256_file


def residual_vector(parameters, times, observed):
    return concentration_model(times, *parameters) - observed


def check_fit_result(result):
    if not result.success:
        raise RuntimeError('Optimization failed: ' + str(result.message))
    if not np.all(np.isfinite(result.x)) or not np.isfinite(result.cost):
        raise ValueError('Non-finite optimization result')
    return result.x.copy()


def least_squares_diagnostics(times, observed, max_nfev=1000, ftol=1e-8, xtol=1e-8, gtol=1e-8):
    """Return OptimizeResult even when not converged: caller must inspect success/status."""
    return least_squares(residual_vector, [1.0, 0.2], args=(np.asarray(times), np.asarray(observed)),
                         bounds=([0., 0.], [np.inf, np.inf]), max_nfev=max_nfev,
                         ftol=ftol, xtol=xtol, gtol=gtol)


def align_measurements(measurements, factors):
    """Align factors by sample ID, reject absent and duplicate labels before arithmetic."""
    if not measurements.index.is_unique or not factors.index.is_unique:
        raise ValueError('Duplicate sample IDs')
    aligned = factors.reindex(measurements.index)
    if aligned.isna().any() or measurements.isna().any():
        raise ValueError('Unmatched or missing sample measurements')
    return measurements * aligned


def fit_reaction(frame, initial_guess=(1.0, 0.2)):
    required = ['time_s', 'observed']
    if not set(required).issubset(frame.columns):
        raise ValueError('Required columns are missing')
    if frame.empty:
        raise ValueError('Input data is empty')
    ordered = frame.sort_values('time_s').reset_index(drop=True)
    values = ordered[required].to_numpy(dtype=np.float64, copy=True)
    if not np.all(np.isfinite(values)):
        raise ValueError('Non-finite measurements')
    times, observed = values[:, 0], values[:, 1]
    if np.any(times < 0) or np.any(observed < 0):
        raise ValueError('Invalid data range')
    if np.unique(times).size != times.size:
        raise ValueError('Duplicate time values')
    if len(times) < 3:
        raise ValueError('At least three observations required')
    parameters, covariance = curve_fit(concentration_model, times, observed, p0=initial_guess,
                                       bounds=([0., 0.], [np.inf, np.inf]))
    if not np.all(np.isfinite(parameters)):
        raise ValueError('Non-finite parameters')
    predicted = concentration_model(times, *parameters)
    result_frame = ordered.copy()
    result_frame['predicted'] = predicted
    result_frame['residual'] = observed - predicted
    return parameters, covariance, result_frame


def run_analysis(input_path: Path, output_dir: Path) -> dict:
    """Section 13.8.3 script flow; based on manuscript with explicit validation."""
    input_path, output_dir = Path(input_path), Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    frame = pd.read_csv(input_path)
    initial_guess = (1.0, 0.2)
    parameters, covariance, results = fit_reaction(frame, initial_guess)
    c0_est, k_est = parameters
    residuals = results['residual'].to_numpy(dtype=np.float64)
    sse = float(np.sum(residuals**2))
    rmse = float(np.sqrt(np.mean(residuals**2)))
    output_path = output_dir / 'reaction_fit_results.csv'
    results.to_csv(output_path, index=False)
    record = {
      'created_at_utc': datetime.now(timezone.utc).isoformat(),
      'model': 'first_order_decay',
      'optimizer': 'scipy.optimize.curve_fit',
      'initial_guess': list(initial_guess),
      'bounds': {'lower': [0.0, 0.0], 'upper': [None, None]},
      'parameters': {'c0': float(c0_est), 'k': float(k_est)},
      'metrics': {'sse': sse, 'rmse': rmse},
      'input': {'file': str(input_path), 'sha256': sha256_file(input_path)},
      'output': {'file': str(output_path), 'sha256': sha256_file(output_path)},
      'environment': {'python': sys.version.split()[0], 'numpy': np.__version__,
                      'scipy': scipy.__version__, 'pandas': pd.__version__, 'platform': platform.platform()}}
    with (output_dir / 'run_metadata.json').open('w', encoding='utf-8') as file:
        json.dump(record, file, indent=2, ensure_ascii=False, allow_nan=False)
    return record
