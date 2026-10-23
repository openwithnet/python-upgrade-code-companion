"""Chapter 13 SciPy/pandas reviewed representative executable examples.
Based on teaching patterns in sections 13.2, 13.4, 13.5–13.8;
not a verbatim extraction of the full manuscript.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.integrate import solve_ivp


def concentration_model(t, c0, k):
    return c0 * np.exp(-k * np.asarray(t, dtype=float))


def fit_decay(times, observed, p0=(1., .2)):
    t = np.asarray(times, dtype=float)
    y = np.asarray(observed, dtype=float)
    if t.ndim != 1 or y.ndim != 1 or t.size != y.size or t.size < 3:
        raise ValueError('times and observed must be aligned 1D vectors (at least 3 samples)')
    if not (np.isfinite(t).all() and np.isfinite(y).all()):
        raise ValueError('non-finite value')
    return curve_fit(concentration_model, t, y, p0=p0, bounds=([0., 0.], [np.inf, np.inf]))


def reaction_rhs(t, y, k):
    return -k * np.asarray(y)


def integrate_decay(k=.2, c0=1., t_eval=None):
    if t_eval is None:
        t_eval = np.linspace(0, 5, 6)
    t_eval = np.asarray(t_eval, dtype=float)
    if t_eval.ndim != 1 or len(t_eval) < 2 or not np.isfinite(t_eval).all() or np.any(np.diff(t_eval) <= 0):
        raise ValueError('strictly increasing time grid required')
    solution = solve_ivp(reaction_rhs, (t_eval[0], t_eval[-1]), [c0], args=(k,), t_eval=t_eval, rtol=1e-9, atol=1e-12)
    if not solution.success:
        raise RuntimeError(solution.message)
    return solution


def assemble_results(times, observed, c0, k):
    t = np.asarray(times, dtype=float)
    obs = np.asarray(observed, dtype=float)
    if t.shape != obs.shape:
        raise ValueError('length mismatch')
    pred = concentration_model(t, c0, k)
    frame = pd.DataFrame({'time': t, 'observed': obs, 'predicted': pred, 'residual': obs - pred})
    rmse = float(np.sqrt(np.mean(frame['residual'].to_numpy()**2)))
    return frame, rmse


def sha256_file(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def save_analysis(frame, output_dir):
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    csv = out / 'reaction_fit_results.csv'
    frame.to_csv(csv, index=False)
    record = {'output_file': str(csv), 'sha256': sha256_file(csv), 'n_rows': len(frame)}
    (out / 'run_metadata.json').write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding='utf-8')
    return record
