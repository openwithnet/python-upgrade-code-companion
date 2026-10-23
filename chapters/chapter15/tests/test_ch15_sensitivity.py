import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"src"))
import numpy as np
import pytest
from ch15_sensitivity import default_example,numpy_concentration,analytical_jacobian,torch_jacobian,jax_jacobian

def test_concentration():
    t,p=default_example();np.testing.assert_allclose(numpy_concentration(t,p),np.exp(-.2*t))
def test_analytical_shape():
    t,p=default_example();assert analytical_jacobian(t,p).shape==(5,2)
def test_first_row():
    t,p=default_example();np.testing.assert_allclose(analytical_jacobian(t,p)[0],[1.,0.])
def test_analytical_finite_difference():
    t,p=default_example();h=1e-6; cols=[]
    for i in range(2):
        d=np.zeros(2);d[i]=h;cols.append((numpy_concentration(t,p+d)-numpy_concentration(t,p-d))/(2*h))
    np.testing.assert_allclose(analytical_jacobian(t,p),np.column_stack(cols),rtol=1e-9,atol=1e-9)
def test_torch():
    pytest.importorskip("torch");t,p=default_example();np.testing.assert_allclose(torch_jacobian(t,p),analytical_jacobian(t,p),atol=1e-12,rtol=1e-12)
def test_jax():
    pytest.importorskip("jax");t,p=default_example();np.testing.assert_allclose(jax_jacobian(t,p),analytical_jacobian(t,p),atol=1e-12,rtol=1e-12)
def test_jax_jit():
    pytest.importorskip("jax");t,p=default_example();np.testing.assert_allclose(jax_jacobian(t,p,True),analytical_jacobian(t,p),atol=1e-12,rtol=1e-12)
