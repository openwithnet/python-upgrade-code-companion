# CODE_COMPANION_ROLE: REFERENCE
# CODE_COMPANION_PROVENANCE: RECOVERED_V72
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""Educational first-order A -> B kinetics; concentration in mol/L, time in s."""
from __future__ import annotations
from dataclasses import dataclass
from math import exp, isfinite
from typing import Protocol


def nonnegative_finite(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric")
    try:
        x = float(value)
    except OverflowError as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not isfinite(x) or x < 0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return x

class RateLaw(Protocol):
    def rate(self, concentration: float) -> float: ...

@dataclass(frozen=True)
class FirstOrderRate:
    k: float  # s^-1
    def __post_init__(self) -> None:
        object.__setattr__(self, "k", nonnegative_finite(self.k, "k"))
    def rate(self, concentration: float) -> float:
        c = nonnegative_finite(concentration, "concentration")
        r = self.k * c
        if not isfinite(r):
            raise ValueError("rate overflow")
        return r

@dataclass(frozen=True)
class Trajectory:
    times: tuple[float, ...]
    concentrations: tuple[float, ...]


def simulate_euler(model: RateLaw, c0: float, dt: float, steps: int) -> Trajectory:
    c = nonnegative_finite(c0, "c0")
    h = nonnegative_finite(dt, "dt")
    if h == 0:
        raise ValueError("dt must be positive")
    if isinstance(steps, bool) or not isinstance(steps, int):
        raise TypeError("steps must be an integer")
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    times, values = [0.0], [c]
    for i in range(1, steps + 1):
        rate = nonnegative_finite(model.rate(c), "rate")
        new_c = c - h * rate
        t = i * h
        if not isfinite(t):
            raise ValueError("time overflow")
        if new_c < 0:
            raise ValueError("Euler step makes concentration negative; reduce dt")
        c = nonnegative_finite(new_c, "concentration")
        times.append(t)
        values.append(c)
    return Trajectory(tuple(times), tuple(values))


def exact_first_order(c0: float, k: float, t: float) -> float:
    c0 = nonnegative_finite(c0, "c0")
    k = nonnegative_finite(k, "k")
    t = nonnegative_finite(t, "t")
    return c0 * exp(-k * t)


def main() -> None:
    model = FirstOrderRate(0.2)
    path = simulate_euler(model, c0=1.0, dt=1.0, steps=5)
    for t, c in zip(path.times, path.concentrations):
        print(f"t={t:.0f} s  Euler={c:.6f}  exact={exact_first_order(1.0, model.k, t):.6f}")

if __name__ == '__main__':
    main()
