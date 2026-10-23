"""Chapter 12 additional runnable excerpts reconstructed from the Word manuscript.

12.3.3 and 12.6.2; scientific contracts are exactly as stated in these excerpts.
"""
import numpy as np

def apply_experiment_scales(
    data: np.ndarray,
    scales: np.ndarray,
) -> np.ndarray:

    if data.ndim != 2:
        raise ValueError(
            "data must be a 2D array"
        )

    if scales.ndim != 1:
        raise ValueError(
            "scales must be a 1D array"
        )

    if data.shape[0] != scales.shape[0]:
        raise ValueError(
            "number of experiments does not match"
        )

    return data * scales[:, None]

def scale_in_chunks(
    values: np.ndarray,
    factor: float,
    chunk_size: int = 100_000,
) -> np.ndarray:

    if values.ndim != 1:
        raise ValueError("1D array required")

    if chunk_size <= 0:
        raise ValueError(
            "chunk_size must be positive"
        )

    result = np.empty_like(
        values,
        dtype=np.float64,
    )

    for start in range(
        0,
        values.size,
        chunk_size,
    ):
        stop = min(
            start + chunk_size,
            values.size,
        )

        result[start:stop] = (
            values[start:stop] * factor
        )

    return result
