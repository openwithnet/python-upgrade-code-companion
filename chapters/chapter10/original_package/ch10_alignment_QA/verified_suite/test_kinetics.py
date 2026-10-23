import math
import pytest
from kinetics import FirstOrderRate, exact_first_order, simulate_euler

def test_rate():
    assert FirstOrderRate(0.2).rate(3.0) == pytest.approx(0.6)

def test_initial():
    p = simulate_euler(FirstOrderRate(.2), 1., 1., 0)
    assert p.times == (0.,) and p.concentrations == (1.,)

def test_euler():
    p = simulate_euler(FirstOrderRate(.2), 1., 1., 3)
    assert p.concentrations == pytest.approx((1., .8, .64, .512))

def test_exact():
    assert exact_first_order(1., .2, 5.) == pytest.approx(math.exp(-1))

def test_zero_rate():
    assert simulate_euler(FirstOrderRate(0), 3., 1., 2).concentrations == (3.,3.,3.)

@pytest.mark.parametrize('bad',[-1.,float('nan'),float('inf')])
def test_bad_coeff(bad):
    with pytest.raises(ValueError): FirstOrderRate(bad)

def test_bad_bool():
    with pytest.raises(TypeError): FirstOrderRate(True)

def test_step_too_large():
    with pytest.raises(ValueError, match='reduce dt'): simulate_euler(FirstOrderRate(.2),1.,6.,2)

def test_bad_step_count():
    with pytest.raises(TypeError): simulate_euler(FirstOrderRate(.2),1.,1.,True)

def test_step_refinement():
    m=FirstOrderRate(.2)
    coarse=simulate_euler(m,1.,1.,5).concentrations[-1]
    fine=simulate_euler(m,1.,.1,50).concentrations[-1]
    exact=exact_first_order(1.,.2,5.)
    assert abs(fine-exact)<abs(coarse-exact)
