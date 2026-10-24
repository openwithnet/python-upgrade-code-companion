# CODE_COMPANION_ROLE: REFERENCE
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""Chapter 12 §12.2, 12.6.3, 12.7, 12.9.3 manuscript-aligned examples.
The benchmark returns measurements, not a universal speed guarantee.
"""
import numpy as np
from time import perf_counter


def shape_axis_reduction():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    return a.ndim, a.shape, a.size, a.mean(axis=0), a.mean(axis=1)


def simulate_euler(c0: float, k: float, dt: float, steps: int) -> np.ndarray:
    """Transcribed from §12.6.3; dt*k <= 1 prevents negative example concentrations."""
    if not np.isfinite(c0) or c0 < 0: raise ValueError("invalid c0")
    if not np.isfinite(k) or k < 0: raise ValueError("invalid k")
    if not np.isfinite(dt) or dt <= 0: raise ValueError("invalid dt")
    if isinstance(steps, bool) or not isinstance(steps, int):
        raise TypeError("steps must be an integer")
    if steps < 0: raise ValueError("steps must be nonnegative")
    if dt * k > 1.0: raise ValueError("dt * k must not exceed 1")
    concentrations = np.empty(steps + 1, dtype=np.float64)
    concentrations[0] = c0
    for i in range(steps):
        c = concentrations[i]
        concentrations[i + 1] = c - dt * k * c
    return concentrations


def floating_point_examples():
    a, b = 1.0e16, 1.0
    return (a+b)-a, np.float32(0.1), np.float64(0.1)


def positions_with_loop(times, x0, v0, a):
    return np.asarray([x0+v0*t+0.5*a*t*t for t in times], dtype=float)


def positions_vectorized(times, x0, v0, a):
    t = np.asarray(times, dtype=float)
    return x0 + v0*t + 0.5*a*t**2


def compare_position_methods(n=10_000, repeats=3):
    if not isinstance(n, int) or isinstance(n,bool) or n<=0: raise ValueError('n must be positive')
    if not isinstance(repeats, int) or isinstance(repeats,bool) or repeats<=0: raise ValueError('repeats must be positive')
    ts = np.linspace(0.0,10.0,n)
    x0,v0,a=2.0,3.0,-1.0
    positions_with_loop(ts[:10],x0,v0,a)
    positions_vectorized(ts[:10],x0,v0,a)
    pairs=[]
    for _ in range(repeats):
        start=perf_counter(); loop=positions_with_loop(ts,x0,v0,a); loop_time=perf_counter()-start
        start=perf_counter(); vector=positions_vectorized(ts,x0,v0,a); vector_time=perf_counter()-start
        np.testing.assert_allclose(loop,vector)
        pairs.append((loop_time,vector_time))
    return np.array(pairs)
