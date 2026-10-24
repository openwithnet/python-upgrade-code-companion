# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
import math
import unittest
from c3_calibration import (
    CalibrationModel, LinearCalibration, QuadraticCalibration,
    analyze_signal, analyze_many, finite_real,
)


class CalibrationTests(unittest.TestCase):
    def test_linear_example(self):
        self.assertEqual(analyze_signal(9, LinearCalibration(2, 1)), 4)

    def test_quadratic_example(self):
        self.assertEqual(analyze_signal(9, QuadraticCalibration(2, 1)), 2)

    def test_linear_batch(self):
        self.assertEqual(analyze_many([1, 3, 9], LinearCalibration(2, 1)), [0, 1, 4])

    def test_quadratic_batch(self):
        self.assertEqual(analyze_many([1, 3, 9], QuadraticCalibration(2, 1)), [0, 1, 2])

    def test_zero_concentration(self):
        for cls in (LinearCalibration, QuadraticCalibration):
            self.assertEqual(cls(2, 1).predict_concentration(1), 0)

    def test_negative_signal_if_intercept_negative(self):
        self.assertEqual(LinearCalibration(2, -3).predict_concentration(-1), 1)

    def test_invalid_slope(self):
        with self.assertRaises(ValueError): LinearCalibration(0, 1)
        with self.assertRaises(ValueError): LinearCalibration(-1, 1)

    def test_invalid_coefficient(self):
        with self.assertRaises(ValueError): QuadraticCalibration(0, 1)
        with self.assertRaises(ValueError): QuadraticCalibration(-1, 1)

    def test_invalid_signal(self):
        for cls in (LinearCalibration, QuadraticCalibration):
            with self.assertRaises(ValueError): cls(2, 1).predict_concentration(0)
            with self.assertRaises(ValueError): cls(2, 1).predict_concentration(float('nan'))
            with self.assertRaises(ValueError): cls(2, 1).predict_concentration(float('inf'))

    def test_invalid_type(self):
        with self.assertRaises(TypeError): finite_real(True, 'x')
        with self.assertRaises(TypeError): finite_real('9', 'x')
        with self.assertRaises(TypeError): LinearCalibration(2, 1).predict_concentration(True)

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError): LinearCalibration(float('inf'), 1)
        with self.assertRaises(ValueError): QuadraticCalibration(2, float('nan'))

    def test_immutable(self):
        from dataclasses import FrozenInstanceError
        with self.assertRaises(FrozenInstanceError): LinearCalibration(2, 1).slope = 3

    def test_overflow_result(self):
        with self.assertRaises(ValueError): LinearCalibration(1e-300, 0).predict_concentration(1e300)

    def test_custom_structural_model(self):
        class ConstantModel:
            def predict_concentration(self, signal: float) -> float:
                return 5.0
        self.assertEqual(analyze_signal(9, ConstantModel()), 5)

    def test_type_protocol(self):
        self.assertTrue(hasattr(LinearCalibration, 'predict_concentration'))

    def test_reject_large_integer(self):
        with self.assertRaises(ValueError): finite_real(10**500, 'x')


if __name__ == '__main__':
    unittest.main()
