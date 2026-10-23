import numpy as np
import pytest
from ch12_remaining_examples import (shape_axis_reduction,simulate_euler,floating_point_examples,positions_with_loop,positions_vectorized,compare_position_methods)

def test_axes():
    ndim,shape,size,bycol,byrow=shape_axis_reduction()
    assert (ndim,shape,size)==(2,(2,3),6)
    np.testing.assert_array_equal(bycol,[2.5,3.5,4.5]);np.testing.assert_array_equal(byrow,[2,5])

def test_euler_output():
    np.testing.assert_allclose(simulate_euler(1,.2,1,5),[1,.8,.64,.512,.4096,.32768])

def test_euler_initial_only():
    np.testing.assert_array_equal(simulate_euler(1,.2,1,0),[1])

@pytest.mark.parametrize('args,err', [((1,.2,1,True),TypeError),((1,.2,1,-1),ValueError),((1,.2,0,2),ValueError),((1,2,1,2),ValueError),((-1,.2,1,2),ValueError)])
def test_euler_bad_args(args,err):
    with pytest.raises(err):simulate_euler(*args)

def test_float_cancellation():
    z,f32,f64=floating_point_examples(); assert z==0; assert f32.dtype==np.dtype('float32'); assert f64.dtype==np.dtype('float64')

def test_same_physics():
    t=np.linspace(0,10,151)
    np.testing.assert_allclose(positions_with_loop(t,2,3,-1),positions_vectorized(t,2,3,-1))

def test_benchmark_smoke():
    timings=compare_position_methods(100,2)
    assert timings.shape==(2,2) and np.all(timings>=0)

@pytest.mark.parametrize('n,repeats',[(0,2),(3,0),(True,1)])
def test_benchmark_invalid(n,repeats):
    with pytest.raises(ValueError):compare_position_methods(n,repeats)
