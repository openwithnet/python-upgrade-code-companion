# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import numpy as np
import pytest
from ch12_6_10_verified_examples import *

def test_vectorized_concentration_matches_loop():
    t=np.arange(4,dtype=float)
    np.testing.assert_allclose(concentration(t), [math_exp(-0.2*x) for x in t])
def math_exp(x):
    import math
    return math.exp(x)
def test_concentration_manuscript_output():
    np.testing.assert_array_equal(np.round(concentration([0,1,2,3]),6), [1.,.818731,.670320,.548812])
def test_float_order_nonassociative():
    a,b,c=1e16,-1e16,1.
    assert (a+b)+c != a+(b+c)
def test_dtype_precision():
    assert np.finfo(np.float64).eps < np.finfo(np.float32).eps
def test_expression_sample_totals():
    total, *_ = expression_analysis()
    np.testing.assert_array_equal(total,[100,102,100,98])
def test_expression_gene_means():
    _, means,*_ = expression_analysis()
    np.testing.assert_array_equal(means,[24.5,15.,26.25,34.25])
def test_expression_groups_and_ratio():
    _,_,a,b,r = expression_analysis()
    np.testing.assert_allclose(a,[11,19,31.5,39.5]); np.testing.assert_allclose(b,[38,11,21,29])
    np.testing.assert_array_equal(np.round(r,3),[3.455,.579,.667,.734])
def test_analytic_motion_output():
    ts=np.arange(5)
    np.testing.assert_array_equal(exact_positions(ts),[2,4.5,6,6.5,6])
def test_euler_motion_output():
    t,x,v=simulate_euler_motion(2.,3.,-1.,1.,4)
    np.testing.assert_array_equal(x,[2,5,7,8,8]);np.testing.assert_array_equal(v,[3,2,1,0,-1])
def test_euler_fine_error():
    t,x,v=simulate_euler_motion(2.,3.,-1.,.1,40)
    assert max(abs(x-exact_positions(t))) == pytest.approx(.2)
def test_steps_zero():
    t,x,v=simulate_euler_motion(2.,3.,-1.,.1,0)
    np.testing.assert_array_equal(x,[2]);np.testing.assert_array_equal(v,[3])
@pytest.mark.parametrize('bad',[True,-1,1.1])
def test_steps_rejected(bad):
    with pytest.raises(ValueError): simulate_euler_motion(2.,3.,-1.,.1,bad)
@pytest.mark.parametrize('bad',[0,-.1,float('nan')])
def test_dt_rejected(bad):
    with pytest.raises(ValueError): simulate_euler_motion(2.,3.,-1.,bad,4)
