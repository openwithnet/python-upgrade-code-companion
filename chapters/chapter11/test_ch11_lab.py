# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: RECOVERED_V72
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import math
import pytest
from kinetics import FirstOrderRate, simulate_euler, exact_first_order
from ch11_lab import EulerStep, MidpointStep, make_solver, simulate, Recorder

@pytest.mark.parametrize('method', ['euler','midpoint'])
def test_initial_event(method):
    recorder = Recorder()
    path = simulate(FirstOrderRate(.2), 1., 1., 0, make_solver(method), recorder)
    assert path.concentrations == (1.,)
    assert len(recorder.events) == 1 and recorder.events[0].step == 0

def test_euler_agrees_with_canonical():
    model = FirstOrderRate(.2)
    assert simulate(model, 1., 1., 5, EulerStep()) == simulate_euler(model, 1., 1., 5)

def test_midpoint_first_step():
    path = simulate(FirstOrderRate(.2), 1., 1., 1, MidpointStep())
    assert path.concentrations[-1] == pytest.approx(.82)

def test_midpoint_improves_at_five_seconds():
    model = FirstOrderRate(.2)
    exact = exact_first_order(1., .2, 5.)
    euler = simulate(model, 1., 1., 5, EulerStep()).concentrations[-1]
    midpoint = simulate(model, 1., 1., 5, MidpointStep()).concentrations[-1]
    assert abs(midpoint-exact) < abs(euler-exact)

def test_recorder():
    recorder = Recorder()
    path = simulate(FirstOrderRate(.2), 1., 1., 5, EulerStep(), recorder)
    assert len(recorder.events) == 6
    assert [ev.step for ev in recorder.events] == list(range(6))
    assert recorder.events[-1].concentration == path.concentrations[-1]

def test_unknown_solver():
    with pytest.raises(ValueError, match='unknown solver'):
        make_solver('bogus')

@pytest.mark.parametrize('bad',[-1, float('nan'), float('inf')])
def test_bad_dt(bad):
    with pytest.raises(ValueError):
        simulate(FirstOrderRate(.2),1.,bad,1,EulerStep())

def test_bad_steps():
    with pytest.raises(TypeError):
        simulate(FirstOrderRate(.2),1.,1.,True,EulerStep())

def test_midpoint_negative_intermediate():
    with pytest.raises(ValueError, match='midpoint'):
        simulate(FirstOrderRate(.2),1.,20.,1,MidpointStep())

def test_observer_error_propagates():
    def broken(event):
        raise RuntimeError('logger unavailable')
    with pytest.raises(RuntimeError,match='logger unavailable'):
        simulate(FirstOrderRate(.2),1.,1.,1,EulerStep(),broken)
