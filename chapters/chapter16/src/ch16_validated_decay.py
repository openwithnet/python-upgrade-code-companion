import numpy as np

def _numeric_array(value, name):
    def reject_bool(item):
        if isinstance(item, (bool, np.bool_)):
            raise ValueError(f"{name} must not contain boolean values")
        if isinstance(item, (list, tuple)):
            for element in item:
                reject_bool(element)
        elif isinstance(item, np.ndarray):
            if item.dtype.kind == "b":
                raise ValueError(f"{name} must not contain boolean values")
            if item.dtype.kind == "O":
                raise ValueError(f"{name} must contain real numeric values")
    reject_bool(value)
    try:
        raw = np.asarray(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            f"{name} must be numeric"
        ) from exc

    if raw.dtype.kind not in "iuf":
        raise ValueError(
            f"{name} must contain real numeric values"
        )

    try:
        return np.asarray(
            raw,
            dtype=np.float64,
        )
    except (
        TypeError,
        ValueError,
        OverflowError,
    ) as exc:
        raise ValueError(
            f"{name} must be representable as float64"
        ) from exc

def _scalar(value, name):
    data = _numeric_array(
        value,
        name,
    )

    if data.ndim != 0:
        raise ValueError(
            f"{name} must be scalar"
        )

    result = float(data)

    if not np.isfinite(result) or result < 0:
        raise ValueError(
            f"{name} must be finite and nonnegative"
        )

    return result

def _times(value):
    data = _numeric_array(
        value,
        "times",
    )

    if data.ndim not in (0, 1):
        raise ValueError(
            "times must be scalar or one-dimensional"
        )

    if (
        not np.all(np.isfinite(data))
        or np.any(data < 0)
    ):
        raise ValueError(
            "times must be finite and nonnegative"
        )

    return data

def validated_decay(times, c0, k):
    t = _times(times)

    initial = _scalar(
        c0,
        "c0",
    )

    rate = _scalar(
        k,
        "k",
    )

    result = initial * np.exp(
        -rate * t
    )

    if result.ndim == 0:
        return float(result)

    return result
