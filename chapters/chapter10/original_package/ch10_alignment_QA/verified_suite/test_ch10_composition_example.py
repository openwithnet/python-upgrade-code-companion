# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import pytest
from ch10_composition_example import FirstOrderModel, EulerStep, MidpointStep, Simulation

def test_derivative():
    assert FirstOrderModel(.2).derivative(3.) == pytest.approx(-.6)

def test_euler():
    assert Simulation(FirstOrderModel(.2), EulerStep(), 1.).advance(1.) == pytest.approx(.8)

def test_midpoint():
    assert Simulation(FirstOrderModel(.2), MidpointStep(), 1.).advance(1.) == pytest.approx(.82)

def test_solver_injection():
    class RecordingSolver:
        def __init__(self): self.calls = []
        def step(self, c, model, dt):
            self.calls.append((c, model, dt))
            return 7.5
    model, solver = FirstOrderModel(.2), RecordingSolver()
    sim = Simulation(model, solver, .5)
    assert sim.advance(1.) == 7.5
    assert solver.calls == [(1., model, .5)]


def test_euler_constant_derivative_isolated():
    """Word §10.4.4: verify Euler independently of first-order kinetics."""
    class ConstantDerivative:
        def derivative(self, concentration: float) -> float:
            return -0.5

    result = EulerStep().step(2.0, ConstantDerivative(), 1.0)
    assert result == pytest.approx(1.5)
