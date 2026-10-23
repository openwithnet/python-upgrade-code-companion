import pytest
from dataclasses import FrozenInstanceError
from c3_calibration import LinearCalibration, QuadraticCalibration
from c3_validation import SignalMeasurement
from ch10_pipeline import run_analysis, make_demo_report

def test_demo():
    r = make_demo_report()
    assert [i.model_name for i in r.results] == ['linear','quadratic']
    assert r.results[0].concentrations == (0.,1.,4.)
    assert r.results[1].concentrations == (0.,1.,2.)

def test_empty_measurements():
    r = run_analysis([], {'linear': LinearCalibration(2,1)})
    assert r.results[0].concentrations == ()

def test_missing_models():
    with pytest.raises(ValueError): run_analysis([], {})

@pytest.mark.parametrize('name', ['', '  ', 7, None])
def test_bad_model_names(name):
    with pytest.raises(ValueError): run_analysis([], {name: LinearCalibration(2,1)})

def test_bad_measurement_element():
    with pytest.raises(TypeError): run_analysis([9.0], {'linear': LinearCalibration(2,1)})

def test_bad_model():
    with pytest.raises(TypeError): run_analysis([], {'bad': object()})

def test_bad_measurements_container():
    with pytest.raises(TypeError): run_analysis((), {'linear': LinearCalibration(2,1)})

def test_model_failure_is_not_silenced():
    with pytest.raises(ValueError): run_analysis([SignalMeasurement(0.0,'mV')], {'linear': LinearCalibration(2,1)})

def test_report_frozen():
    r = make_demo_report()
    with pytest.raises(FrozenInstanceError): r.results = ()

def test_input_object_unchanged():
    m = SignalMeasurement(0.009,'V')
    run_analysis([m], {'linear': LinearCalibration(2,1)})
    assert (m.value, m.unit) == (0.009,'V')

def test_model_order_and_units():
    r = run_analysis([SignalMeasurement(9.,'mV'), SignalMeasurement(.009,'V')], {'quadratic': QuadraticCalibration(2,1),'linear': LinearCalibration(2,1)})
    assert [x.model_name for x in r.results] == ['quadratic','linear']
    assert r.results[0].concentrations == (2.,2.)
    assert r.results[1].concentrations == (4.,4.)
