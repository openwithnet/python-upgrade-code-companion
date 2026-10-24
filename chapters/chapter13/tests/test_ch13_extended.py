# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import json
import numpy as np
import pandas as pd
import pytest
from pathlib import Path
from ch13_examples import concentration_model, sha256_file
from ch13_extended import (least_squares_diagnostics, check_fit_result, align_measurements, fit_reaction, run_analysis)

def data():
    t = np.linspace(0, 5, 8)
    return t, concentration_model(t, 1.5, 0.3)

def test_fit_converges():
    t, y = data(); result = least_squares_diagnostics(t,y)
    np.testing.assert_allclose(check_fit_result(result), [1.5, .3], atol=1e-6)

def test_evaluation_limit_is_failure():
    t,y=data(); result=least_squares_diagnostics(t,y,max_nfev=1)
    assert not result.success and result.status == 0 and result.nfev == 1
    with pytest.raises(RuntimeError): check_fit_result(result)

def test_tolerances_not_parameter_error_guarantee():
    t,y=data(); result=least_squares_diagnostics(t,y,ftol=1e-7,xtol=1e-7,gtol=1e-7)
    assert result.success

def test_series_auto_alignment():
    a=pd.Series([1.,2.],index=['S01','S02']); b=pd.Series([10.,20.],index=['S02','S03'])
    res=a+b; assert np.isnan(res.loc['S01']) and res.loc['S02']==12 and np.isnan(res.loc['S03'])

def test_explicit_alignment():
    a=pd.Series([10.,20.,30.],index=['S01','S02','S03'])
    b=pd.Series([1.2,.8,1.1],index=['S03','S01','S02'])
    np.testing.assert_allclose(align_measurements(a,b).to_numpy(),[8.,22.,36.])

def test_alignment_rejects_missing():
    with pytest.raises(ValueError): align_measurements(pd.Series([1.],index=['A']),pd.Series([2.],index=['B']))

def test_alignment_rejects_duplicates():
    with pytest.raises(ValueError): align_measurements(pd.Series([1.,2.],index=['A','A']),pd.Series([2.],index=['A']))

def test_fit_reaction_sorts_keeps_correspondence():
    t,y=data(); f=pd.DataFrame({'time_s':t[::-1], 'observed':y[::-1], 'sample_id':np.arange(len(t))[::-1]})
    pars,cov,out=fit_reaction(f)
    np.testing.assert_allclose(pars,[1.5,.3],atol=1e-6)
    assert out.time_s.is_monotonic_increasing and np.allclose(out.observed,y)
    assert (out.sample_id.to_numpy()==np.arange(len(t))).all()

def test_duplicate_time_rejected():
    t,y=data(); f=pd.DataFrame({'time_s':t, 'observed':y}); f.loc[1,'time_s']=f.loc[0,'time_s']
    with pytest.raises(ValueError): fit_reaction(f)

def test_run_analysis_roundtrip(tmp_path):
    t,y=data(); inp=tmp_path/'input.csv'; pd.DataFrame({'time_s':t[::-1],'observed':y[::-1]}).to_csv(inp,index=False)
    record=run_analysis(inp,tmp_path/'results')
    out=tmp_path/'results/reaction_fit_results.csv'
    assert out.exists() and record['input']['sha256']==sha256_file(inp)
    assert record['output']['sha256']==sha256_file(out)
    assert record['metrics']['rmse'] < 1e-6
    meta=json.loads((tmp_path/'results/run_metadata.json').read_text(encoding='utf-8'))
    assert meta['parameters']==record['parameters']

def test_nonfinite_input_rejected():
    with pytest.raises(ValueError): fit_reaction(pd.DataFrame({'time_s':[0.,1.,2.], 'observed':[1.,float('nan'),.5]}))
