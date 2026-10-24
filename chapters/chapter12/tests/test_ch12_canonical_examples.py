# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import numpy as np
from ch12_canonical_examples import decay_vectorized, axis_means, broadcasting

def test_decay():
    np.testing.assert_allclose(decay_vectorized(), np.exp(-0.2*np.arange(6)))
    np.testing.assert_array_equal(np.round(decay_vectorized(), 6), [1.,.818731,.670320,.548812,.449329,.367879])

def test_axis_means():
    a,b=axis_means()
    np.testing.assert_allclose(a,[1.,.8,.6,.5])
    np.testing.assert_allclose(b,[.725,.825,.625])

def test_broadcasting():
    np.testing.assert_array_equal(broadcasting(), [[11,22,33,44],[15,26,37,48],[19,30,41,52]])
