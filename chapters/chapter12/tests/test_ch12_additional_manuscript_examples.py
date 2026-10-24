# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import numpy as np
import pytest
from ch12_additional_manuscript_examples import apply_experiment_scales, scale_in_chunks

def test_scales_values_and_axis():
    data=np.arange(1.,7.).reshape(2,3)
    np.testing.assert_array_equal(apply_experiment_scales(data,np.array([2.,3.])),data*np.array([2.,3.])[:,None])

@pytest.mark.parametrize('data,scales',[(np.ones(3),np.ones(3)),(np.ones((2,3)),np.ones((2,1))),(np.ones((2,3)),np.ones(3))])
def test_scales_invalid_shape(data,scales):
    with pytest.raises(ValueError): apply_experiment_scales(data,scales)

def test_chunked_expected_output():
    np.testing.assert_array_equal(scale_in_chunks(np.array([1.,2.,3.,4.]),2.5,2),[2.5,5.,7.5,10.])

def test_chunk_size_must_be_positive():
    with pytest.raises((ValueError,TypeError)):scale_in_chunks(np.arange(4.),2.0,0)
