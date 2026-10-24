# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""Chapter 10.3-10.4 explanatory one-step composition example.

Distinct from the Chapter 10.5 canonical kinetics.py: this API uses signed
*derivative* dc/dt; kinetics.py uses nonnegative *consumption rate* -dc/dt.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import isfinite
from typing import Protocol

class DerivativeModel(Protocol):
    def derivative(self, concentration: float) -> float: ...

class StepSolver(Protocol):
    def step(self, concentration: float, model: DerivativeModel, dt: float) -> float: ...

@dataclass(frozen=True)
class FirstOrderModel:
    k: float
    def __post_init__(self):
        if not isinstance(self.k, (int, float)) or isinstance(self.k, bool) or not isfinite(self.k) or self.k < 0:
            raise ValueError('k must be finite and nonnegative numeric')
    def derivative(self, concentration: float) -> float:
        return -self.k * concentration

class EulerStep:
    def step(self, concentration: float, model: DerivativeModel, dt: float) -> float:
        return concentration + dt * model.derivative(concentration)

class MidpointStep:
    def step(self, concentration: float, model: DerivativeModel, dt: float) -> float:
        k1 = model.derivative(concentration)
        k2 = model.derivative(concentration + 0.5 * dt * k1)
        return concentration + dt * k2

@dataclass(frozen=True)
class Simulation:
    model: DerivativeModel
    solver: StepSolver
    dt: float
    def advance(self, concentration: float) -> float:
        return self.solver.step(concentration, self.model, self.dt)

if __name__ == '__main__':
    m = FirstOrderModel(0.2)
    print('Euler:', Simulation(m, EulerStep(), 1.0).advance(1.0))
    print('Midpoint:', Simulation(m, MidpointStep(), 1.0).advance(1.0))
