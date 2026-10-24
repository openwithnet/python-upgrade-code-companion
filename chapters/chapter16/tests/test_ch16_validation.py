# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
import pytest
from ch16_initial_bug import buggy_numeric_array, initial_decay
from ch16_validated_decay import _numeric_array,_scalar,_times,validated_decay

def test_bug_reproduced():
    assert np.array_equal(buggy_numeric_array([True, 0]), [1.0, 0.0])

@pytest.mark.parametrize('value', [[True,0],[False,1], [[True,0]], np.array([True,False]), np.array([True,0],dtype=object), ['1',2], [1+0j,2], {'x':1}])
def test_rejected_values(value):
    with pytest.raises(ValueError): _numeric_array(value,'v')

@pytest.mark.parametrize('value', [[0,1], np.array([0.,1.]), (0,1), 2.0, np.int64(2)])
def test_numeric_values(value):
    assert np.all(np.isfinite(_numeric_array(value,'v')))

@pytest.mark.parametrize('value', [-1, np.nan, np.inf, True, '0.2', [0.2]])
def test_scalar_reject(value):
    with pytest.raises(ValueError): _scalar(value,'k')

@pytest.mark.parametrize('value', [-1, np.inf, [0,np.nan], [[0,1]], [False,1], ['0',1]])
def test_times_reject(value):
    with pytest.raises(ValueError): _times(value)

def test_scalar_result():
    result = validated_decay(2,1,.2)
    assert isinstance(result,float) and result == pytest.approx(np.exp(-.4))

def test_vector_result():
    value=validated_decay([0,1,2],1,.2)
    assert value.dtype == np.float64 and np.allclose(value,np.exp(-.2*np.arange(3)))

def test_empty_vector():
    assert validated_decay([],1,.2).shape==(0,)

def test_zero_rate():
    assert np.array_equal(validated_decay([0,1],3,0), [3,3])


def test_manuscript_initial_example_is_intentionally_permissive():
    # Word v37 §16.5.1: 금지된 입력에서도 계산이 수행되는 결함 시연.
    assert np.allclose(initial_decay(["0", "1"], 1.0, 0.2), [1.0, np.exp(-0.2)])
    assert np.allclose(initial_decay([False, True], 1.0, 0.2), [1.0, np.exp(-0.2)])
    with pytest.raises(ValueError):
        validated_decay([False, True], 1.0, 0.2)
    with pytest.raises(ValueError):
        validated_decay(["0", "1"], 1.0, 0.2)
