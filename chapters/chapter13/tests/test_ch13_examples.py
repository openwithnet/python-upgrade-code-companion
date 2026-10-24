# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
import pandas as pd
import pytest
from ch13_examples import concentration_model, fit_decay, integrate_decay, assemble_results, sha256_file, save_analysis

def test_model():
    np.testing.assert_allclose(concentration_model(np.array([0.,1.]),1.,.2), [1., np.exp(-.2)])

def test_fit():
    t=np.linspace(0,5,11)
    params, cov=fit_decay(t,concentration_model(t,1.02,.21))
    np.testing.assert_allclose(params,[1.02,.21],atol=1e-6)
    assert cov.shape==(2,2)

def test_fit_bad_length():
    with pytest.raises(ValueError): fit_decay([0,1,2], [1,2])

def test_fit_nan():
    with pytest.raises(ValueError): fit_decay([0,1,2], [1,float('nan'),2])

def test_ivp():
    sol=integrate_decay()
    assert sol.y.shape==(1,6)
    np.testing.assert_allclose(sol.y[0],np.exp(-.2*np.arange(6)),atol=1e-8)

def test_ivp_bad_times():
    with pytest.raises(ValueError): integrate_decay(t_eval=[0,2,1])

def test_dataframe_rmse():
    frame,rmse=assemble_results([0,1],[1.,np.exp(-.2)],1.,.2)
    assert list(frame.columns)==['time','observed','predicted','residual']
    assert rmse < 1e-14

def test_dataframe_mismatch():
    with pytest.raises(ValueError): assemble_results([0,1],[1],1,.2)

def test_save(tmp_path):
    frame=pd.DataFrame({'time':[0,1], 'value':[1.,.8]})
    r=save_analysis(frame,tmp_path/'results')
    assert r['n_rows']==2
    assert sha256_file(r['output_file'])==r['sha256']
