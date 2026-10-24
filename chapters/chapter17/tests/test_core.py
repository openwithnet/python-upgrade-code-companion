# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: RECONSTRUCTED_NOT_ORIGINAL
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import numpy as np
import pytest
from oscillator_lab import (OscillatorModel, EulerSolver, RK4Solver, SciPySolver, exact_state, energy, real_array)

@pytest.fixture
def model(): return OscillatorModel(1.0,4.0)
@pytest.mark.parametrize('solver',[EulerSolver(),RK4Solver(),SciPySolver()])
def test_contract_shape(model,solver):
    tr=solver.solve(model,[1.,0.],.1,10)
    assert tr.states.shape==(11,2)
    np.testing.assert_allclose(tr.times,np.arange(11)*.1)
@pytest.mark.parametrize('solver',[EulerSolver(),RK4Solver(),SciPySolver()])
def test_zero_steps(model,solver):
    tr=solver.solve(model,[1.,0.],.1,0)
    np.testing.assert_array_equal(tr.states,[[1.,0.]])
@pytest.mark.parametrize('bad', [[True,0], [float('nan'),0], ['1',2]])
def test_bad_state(bad):
    with pytest.raises(ValueError):real_array(bad,'state')
def test_reference(model):
    expected=exact_state(1,model,[1,0])
    tr=SciPySolver().solve(model,[1,0],.1,10)
    np.testing.assert_allclose(tr.states[-1],expected,rtol=1e-7,atol=1e-7)
def test_accuracy_order(model):
    ex=exact_state(1,model,[1,0]);err=[]
    for solver in (EulerSolver(),RK4Solver(),SciPySolver()):
        err.append(np.linalg.norm(solver.solve(model,[1,0],.1,10).states[-1]-ex))
    assert err[2]<err[1]<err[0]
def test_energy(model):
    assert energy(model,[1,0])==pytest.approx(2.)
    result=SciPySolver().solve(model,[1,0],.1,10)
    assert np.max(np.abs(energy(model,result.states)-2))<1e-7
def test_defensive_copy(model):
    tr=SciPySolver().solve(model,[1,0],.1,10)
    a=tr.states; a[0,0]=100
    assert tr.states[0,0]==1
@pytest.mark.parametrize('bad',[True,-1,1.5])
def test_bad_steps(model,bad):
    with pytest.raises(ValueError):SciPySolver().solve(model,[1,0],.1,bad)


def test_scipy_constructor_matches_manuscript(model):
    solver = SciPySolver(method="DOP853", rtol=1e-10, atol=1e-12)
    assert solver.method == "DOP853"
    assert solver.rtol == 1e-10
    assert solver.atol == 1e-12
    tr = solver.solve(model, [1., 0.], .1, 10)
    np.testing.assert_allclose(tr.states[-1], exact_state(1, model, [1., 0.]), atol=1e-8, rtol=1e-8)


def test_scipy_default_tolerances():
    solver = SciPySolver()
    assert solver.method == "RK45"
    assert solver.rtol == 1e-9
    assert solver.atol == 1e-11
