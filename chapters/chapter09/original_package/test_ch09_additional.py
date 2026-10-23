"""Additional Chapter 9 boundary/contract checks, independent of the 32 baseline cases."""
import math
import pytest
from c3_calibration import LinearCalibration, QuadraticCalibration
from c3_validation import SignalMeasurement, analyze_measurements

@pytest.mark.parametrize('model_cls', [LinearCalibration, QuadraticCalibration])
def test_empty_batch(model_cls):
    assert analyze_measurements([], model_cls(2, 1)) == []

@pytest.mark.parametrize('model_cls', [LinearCalibration, QuadraticCalibration])
def test_per_model_intercept(model_cls):
    assert analyze_measurements([SignalMeasurement(4, 'mV')], model_cls(2, 4)) == [0.0]

@pytest.mark.parametrize('model_cls', [LinearCalibration, QuadraticCalibration])
def test_just_below_boundary(model_cls):
    with pytest.raises(ValueError):
        analyze_measurements([SignalMeasurement(math.nextafter(1.0, -math.inf), 'mV')], model_cls(2, 1))

@pytest.mark.parametrize('model_cls', [LinearCalibration, QuadraticCalibration])
def test_negative_coefficients(model_cls):
    with pytest.raises(ValueError): model_cls(-2, 1)

def test_equivalent_units_and_order():
    model = LinearCalibration(2, 1)
    samples = [SignalMeasurement(0.009, 'V'), SignalMeasurement(1, 'mV'), SignalMeasurement(0.003, 'V')]
    assert analyze_measurements(samples, model) == pytest.approx([4, 0, 1])

def test_input_objects_not_mutated():
    samples = [SignalMeasurement(0.009, 'V')]
    analyze_measurements(samples, QuadraticCalibration(2, 1))
    assert samples[0].value == 0.009 and samples[0].unit == 'V'
