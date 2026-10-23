import math
from dataclasses import FrozenInstanceError
import pytest
from c3_calibration import LinearCalibration, QuadraticCalibration, analyze_many, finite_real

@pytest.mark.parametrize('model_type, expected', [
    (LinearCalibration, [0.0, 1.0, 4.0]),
    (QuadraticCalibration, [0.0, 1.0, 2.0]),
])
def test_known_values(model_type, expected):
    actual = analyze_many([1.0, 3.0, 9.0], model_type(2.0, 1.0))
    assert actual == pytest.approx(expected)

@pytest.mark.parametrize('model_type', [LinearCalibration, QuadraticCalibration])
def test_zero_concentration_boundary(model_type):
    model = model_type(2.0, 1.0)
    assert model.predict_concentration(1.0) == pytest.approx(0.0)

@pytest.mark.parametrize('model_type', [LinearCalibration, QuadraticCalibration])
def test_below_intercept(model_type):
    model = model_type(2.0, 1.0)
    with pytest.raises(ValueError, match='zero-concentration'):
        model.predict_concentration(0.0)

@pytest.mark.parametrize('bad', ['9', True, None, float('nan'), float('inf')])
def test_invalid_signal(bad):
    model = LinearCalibration(2.0, 1.0)
    with pytest.raises((TypeError, ValueError)):
        model.predict_concentration(bad)

@pytest.mark.parametrize('model_type', [LinearCalibration, QuadraticCalibration])
def test_invalid_coefficient(model_type):
    with pytest.raises(ValueError, match='positive'):
        model_type(0.0, 1.0)

@pytest.mark.parametrize('model_type', [LinearCalibration, QuadraticCalibration])
def test_frozen_parameters(model_type):
    model = model_type(2.0, 1.0)
    with pytest.raises(FrozenInstanceError):
        model.intercept = 9.0

def test_math_isclose_for_known_solution():
    model = LinearCalibration(2.0, 1.0)
    assert math.isclose(model.predict_concentration(9.0), 4.0, rel_tol=1e-12, abs_tol=1e-12)
