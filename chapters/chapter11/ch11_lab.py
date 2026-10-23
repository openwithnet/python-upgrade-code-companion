"""Chapter 11.6: replaceable numerical strategies, first-order kinetics.

Units: concentration mol/L, time s, first-order k s^-1.
Uses unchanged canonical kinetics.py from Chapter 10.5.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import isfinite
from typing import Protocol
from kinetics import FirstOrderRate, RateLaw, Trajectory, nonnegative_finite, exact_first_order, simulate_euler

class StepStrategy(Protocol):
    def step(self, c: float, dt: float, model: RateLaw) -> float: ...

class EulerStep:
    def step(self, c: float, dt: float, model: RateLaw) -> float:
        return c - dt * model.rate(c)

class MidpointStep:
    def step(self, c: float, dt: float, model: RateLaw) -> float:
        midpoint = c - 0.5 * dt * model.rate(c)
        if not isfinite(midpoint) or midpoint < 0:
            raise ValueError('midpoint concentration invalid; reduce dt')
        return c - dt * model.rate(midpoint)

SOLVERS: dict[str, type[EulerStep] | type[MidpointStep]] = {'euler': EulerStep, 'midpoint': MidpointStep}

def make_solver(name: str) -> StepStrategy:
    try:
        return SOLVERS[name]()
    except KeyError as exc:
        raise ValueError(f'unknown solver: {name!r}') from exc

@dataclass(frozen=True)
class StepEvent:
    step: int
    time: float
    concentration: float

class EventObserver(Protocol):
    def __call__(self, event: StepEvent) -> None: ...

def simulate(model: RateLaw, c0: float, dt: float, steps: int,
             solver: StepStrategy, observer: EventObserver | None = None) -> Trajectory:
    c = nonnegative_finite(c0, 'c0')
    h = nonnegative_finite(dt, 'dt')
    if h == 0: raise ValueError('dt must be positive')
    if isinstance(steps, bool) or not isinstance(steps, int):
        raise TypeError('steps must be an integer')
    if steps < 0: raise ValueError('steps must be nonnegative')
    times, concentrations = [0.0], [c]
    if observer is not None: observer(StepEvent(0, 0.0, c))
    for i in range(1, steps + 1):
        t = i * h
        if not isfinite(t): raise ValueError('time overflow')
        new_c = nonnegative_finite(solver.step(c, h, model), 'concentration')
        c = new_c
        times.append(t)
        concentrations.append(c)
        if observer is not None: observer(StepEvent(i, t, c))
    return Trajectory(tuple(times), tuple(concentrations))

class Recorder:
    def __init__(self) -> None:
        self.events: list[StepEvent] = []
    def __call__(self, event: StepEvent) -> None:
        self.events.append(event)

def run_demo() -> None:
    model = FirstOrderRate(k=0.2)
    for name in ('euler', 'midpoint'):
        recorder = Recorder()
        path = simulate(model, 1.0, 1.0, 5, make_solver(name), recorder)
        print(f'{name:8} final={path.concentrations[-1]:.6f} '
              f'exact={exact_first_order(1.0, model.k, 5.0):.6f} '
              f'events={len(recorder.events)}')
    original = simulate_euler(model, 1.0, 1.0, 5)
    print(f'canonical_euler_final={original.concentrations[-1]:.6f}')

if __name__ == '__main__':
    run_demo()
