# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import numpy as np
import pytest
from ch14_advanced import (compare_estimators, MeanRegressor, fit_and_predict,
                           build_pipeline, pipeline_without_leakage, run_sequence_analysis,
                           RAW_SEQUENCES)

def test_estimator_interchangeability():
    d = compare_estimators()
    assert d['LinearRegression'] == pytest.approx(13)
    assert d['Ridge'] == pytest.approx(12.621621621621621)

def test_mean_regressor_protocol():
    x = np.arange(4.).reshape(-1,1)
    assert np.allclose(fit_and_predict(MeanRegressor(),x,[2,4,6,8],[[4],[5]]),[5,5])

def test_mean_regressor_unfitted():
    with pytest.raises(RuntimeError): MeanRegressor().predict([[2]])

def test_mean_regressor_shape_validation():
    m=MeanRegressor().fit([[1],[2]],[1,2])
    with pytest.raises(ValueError):m.predict([[1,2]])

def test_pipeline_fits_scaler_on_train_only():
    train=np.array([[0.],[2.],[4.]])
    test=np.array([[1000.]])
    p,pred = pipeline_without_leakage(train,[1.,2.,3.],test)
    assert p.named_steps['scaler'].mean_[0] == pytest.approx(2.)
    assert pred.shape == (1,)

def test_pipeline_interface():
    p=build_pipeline()
    assert [name for name,_ in p.steps]==['scaler','regressor']

def test_sequences_have_identity_and_shape():
    d=run_sequence_analysis()
    assert len(RAW_SEQUENCES)==12
    assert d['X'].shape==(12,2)
    assert d['ids']==['S10','S11','S12']

def test_gc_unit_is_percent():
    d=run_sequence_analysis()
    assert d['X'][0,1]==0
    assert d['X'][2,1]==100

def test_analysis_scaler_train_only():
    d=run_sequence_analysis()
    assert np.allclose(d['scaler_mean'],d['X'][:9].mean(axis=0))

def test_predictions_are_finite():
    d=run_sequence_analysis()
    assert np.isfinite(d['predictions']).all()
    assert np.isfinite(d['rmse'])
