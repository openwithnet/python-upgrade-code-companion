"""교육용 의도적 결함 — 최종 구현에 사용하지 마십시오."""
import numpy as np
def buggy_numeric_array(value):
    raw = np.asarray(value)
    if raw.dtype.kind not in "iuf":
        raise ValueError("numeric input required")
    return np.asarray(raw, dtype=np.float64)


def initial_decay(times, c0, k):
    """원고 16.5.1의 *의도적으로 미검증된* 초기 계산을 재현한다.

    문자열·불리언·음수·NaN 등의 입력 계약을 확인하지 않는다.
    실제 연구 계산에는 validated_decay를 사용한다.
    """
    t = np.asarray(times, dtype=np.float64)
    return c0 * np.exp(-k * t)
