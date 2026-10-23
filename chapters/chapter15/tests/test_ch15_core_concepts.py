import numpy as np
import pytest
from ch15_core_concepts import (torch_backward_example,torch_tensor_numpy_copy,jax_functional_grad,jax_array_update,derivative_comparison,three_library_decay)

def test_torch_backward_value():
    assert torch_backward_example()[:2] == (15.0,8.0)
def test_torch_gradient_accumulates():
    assert torch_backward_example()[2] == 16.0
def test_torch_gradient_reset():
    assert torch_backward_example()[3] == 8.0
def test_torch_shared_numpy_storage():
    assert torch_tensor_numpy_copy() == (True,True)
def test_jax_grad():
    assert jax_functional_grad()[0] == pytest.approx(8)
def test_jax_jit():
    a,b=jax_functional_grad(); assert b == pytest.approx(a)
def test_jax_immutable_update():
    a,b=jax_array_update(); assert np.array_equal(a,[1,2,3]);assert np.array_equal(b,[7,2,3])
def test_finite_diff():
    a,b=derivative_comparison();assert b == pytest.approx(a,abs=1e-8)
def test_reject_bad_step():
    with pytest.raises(ValueError):derivative_comparison(h=0)
def test_three_library_results():
    n,p,j=three_library_decay([0,1,2]);assert np.allclose(n,p,atol=1e-12);assert np.allclose(n,j,atol=1e-6)
def test_three_library_initial():
    n,p,j=three_library_decay([0]);assert n[0] == pytest.approx(1);assert p[0] == pytest.approx(1);assert j[0] == pytest.approx(1)
