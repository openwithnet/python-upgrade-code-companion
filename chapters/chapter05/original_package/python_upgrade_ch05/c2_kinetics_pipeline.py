# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""Chapter 5 C2 — function-oriented analysis of kinetic observations.

Python >=3.10; NumPy >=1.24. Input times in min, concentrations in mmol/L.
The synthetic observations are instructional, not measured experimental data.
"""
from __future__ import annotations
import math
from collections.abc import Callable
from typing import TypedDict
import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.float64]

class KineticResult(TypedDict):
    interval_start: FloatArray
    interval_end: FloatArray
    interval_midpoint: FloatArray
    interval_rate: FloatArray

def validate_kinetic_data(times: FloatArray, concentrations: FloatArray) -> None:
    """Require 1D equal-length finite real arrays, >=2 points, t>=0, C>=0, increasing t.

    This is an educational policy for nonnegative concentrations, not a universal
    rule for background-corrected experimental observations.
    """
    for name, array in (("times", times), ("concentrations", concentrations)):
        if not isinstance(array, np.ndarray):
            raise TypeError(f"{name} must be a NumPy array")
        if array.ndim != 1:
            raise ValueError(f"{name} must be one-dimensional")
        if not np.issubdtype(array.dtype, np.number) or np.issubdtype(array.dtype, np.complexfloating):
            raise TypeError(f"{name} must contain real numeric values")
        if not np.isfinite(array).all():
            raise ValueError(f"{name} must be finite")
    if len(times) != len(concentrations):
        raise ValueError("array lengths must match")
    if len(times) < 2:
        raise ValueError("at least two observations are required")
    if np.any(times < 0):
        raise ValueError("times must be nonnegative")
    if np.any(concentrations < 0):
        raise ValueError("concentrations must be nonnegative")
    if not np.all(np.diff(times) > 0):
        raise ValueError("times must be strictly increasing")

def calculate_interval_rates(times: FloatArray, concentrations: FloatArray) -> FloatArray:
    """Compute positive reactant consumption rate -delta(C)/delta(t), with validation."""
    validate_kinetic_data(times, concentrations)
    return -np.diff(concentrations) / np.diff(times)

def analyze_kinetics(times: FloatArray, concentrations: FloatArray) -> KineticResult:
    """Return independent arrays of interval boundaries, midpoints and mean rates."""
    validate_kinetic_data(times, concentrations)
    rates = -np.diff(concentrations) / np.diff(times)
    # This averaging avoids overflow for unusually large finite time values.
    midpoints = times[:-1] + (times[1:] - times[:-1]) / 2.0
    return {"interval_start": times[:-1].copy(),
            "interval_end": times[1:].copy(),
            "interval_midpoint": midpoints.copy(),
            "interval_rate": rates.copy()}

def make_first_order_model(initial_concentration: float,
                           rate_constant: float) -> Callable[[float], float]:
    """Return C(t)=C0 exp(-kt), with C0 in mmol/L, k in min^-1 and t in min."""
    if not math.isfinite(initial_concentration) or initial_concentration < 0:
        raise ValueError("initial concentration must be nonnegative and finite")
    if not math.isfinite(rate_constant) or rate_constant < 0:
        raise ValueError("rate constant must be nonnegative and finite")
    def concentration_at(time: float) -> float:
        if not math.isfinite(time) or time < 0:
            raise ValueError("time must be nonnegative and finite")
        return initial_concentration * math.exp(-rate_constant * time)
    return concentration_at

def main() -> None:
    times = np.array([0., 1., 2., 3., 4.], dtype=np.float64)
    concentrations = np.array([10., 8.2, 6.7, 5.5, 4.6], dtype=np.float64)
    result = analyze_kinetics(times, concentrations)
    print("Interval       Midpoint     Rate")
    for start, end, midpoint, rate in zip(result["interval_start"], result["interval_end"],
                                          result["interval_midpoint"], result["interval_rate"], strict=True):
        print(f"{start:4.1f}-{end:4.1f}        {midpoint:5.2f}       {rate:5.3f}")
    model = make_first_order_model(10.0, 0.2)
    print("\nFirst-order model comparison")
    for time in times:
        print(f"t={time:4.1f}  C_model={model(float(time)):7.4f}")

if __name__ == '__main__':
    main()
