# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import math
from dataclasses import FrozenInstanceError
import pytest
from c3_calibration import LinearCalibration, QuadraticCalibration
from c3_validation import SignalMeasurement, analyze_measurements

@pytest.mark.parametrize('model,expected', [
    (LinearCalibration(2.0,1.0), [0.0,1.0,4.0]),
    (QuadraticCalibration(2.0,1.0), [0.0,1.0,2.0]),
])
def test_known_regression(model, expected):
    inputs=[SignalMeasurement(0.001,'V'), SignalMeasurement(3,'mV'), SignalMeasurement(0.009,'V')]
    assert analyze_measurements(inputs,model) == pytest.approx(expected,rel=1e-12,abs=1e-12)

@pytest.mark.parametrize('bad', ['9',None,True,float('nan'),float('inf')])
def test_bad_measurement(bad):
    error=TypeError if bad in ('9',None,True) else ValueError
    with pytest.raises(error): SignalMeasurement(bad,'mV')

@pytest.mark.parametrize('unit', ['mv','volts','',None])
def test_bad_unit(unit):
    with pytest.raises(ValueError): SignalMeasurement(9,unit)

def test_boundary():
    assert analyze_measurements([SignalMeasurement(1,'mV')],LinearCalibration(2,1)) == [0.0]

def test_outside_domain():
    with pytest.raises(ValueError): analyze_measurements([SignalMeasurement(0,'mV')],QuadraticCalibration(2,1))

def test_overflow_unit_conversion():
    with pytest.raises(ValueError): SignalMeasurement(1e308,'V').as_millivolts()

def test_frozen():
    sample=SignalMeasurement(3,'mV')
    with pytest.raises(FrozenInstanceError): sample.value=4

def test_both_models_inverse_consistency():
    for c in (0.0,1.0,2.0,4.0):
        lin=LinearCalibration(2,1)
        quad=QuadraticCalibration(2,1)
        assert math.isclose(lin.predict_concentration(2*c+1),c,abs_tol=1e-12)
        assert math.isclose(quad.predict_concentration(2*c*c+1),c,abs_tol=1e-12)
