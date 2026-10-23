import unittest
import math
import numpy as np
from c2_kinetics_pipeline import (
    validate_kinetic_data, calculate_interval_rates, analyze_kinetics,
    make_first_order_model,
)

class TestKinetics(unittest.TestCase):
    def setUp(self):
        self.t = np.array([0.,1.,2.,3.,4.])
        self.c = np.array([10.,8.2,6.7,5.5,4.6])
    def test_rates(self):
        np.testing.assert_allclose(calculate_interval_rates(self.t,self.c), [1.8,1.5,1.2,0.9])
    def test_midpoints(self):
        np.testing.assert_allclose(analyze_kinetics(self.t,self.c)['interval_midpoint'],[.5,1.5,2.5,3.5])
    def test_boundaries(self):
        r=analyze_kinetics(self.t,self.c)
        np.testing.assert_array_equal(r['interval_start'],[0,1,2,3])
        np.testing.assert_array_equal(r['interval_end'],[1,2,3,4])
    def test_input_unchanged(self):
        t=self.t.copy(); c=self.c.copy();analyze_kinetics(t,c)
        np.testing.assert_array_equal(t,self.t);np.testing.assert_array_equal(c,self.c)
    def test_returned_arrays_independent(self):
        r=analyze_kinetics(self.t,self.c);r['interval_start'][0]=99
        self.assertEqual(self.t[0],0)
    def test_model(self):
        f=make_first_order_model(10,.2)
        self.assertTrue(math.isclose(f(4), 10*math.exp(-.8)))
    def test_model_initial(self):self.assertEqual(make_first_order_model(10,.2)(0),10)
    def test_model_zero_rate(self):self.assertEqual(make_first_order_model(10,0)(5),10)
    def test_model_negative_time(self):
        with self.assertRaises(ValueError):make_first_order_model(10,.2)(-1)
    def test_model_negative_c0(self):
        with self.assertRaises(ValueError):make_first_order_model(-1,.2)
    def test_model_negative_k(self):
        with self.assertRaises(ValueError):make_first_order_model(10,-.2)
    def test_model_nonfinite(self):
        with self.assertRaises(ValueError):make_first_order_model(float('nan'),.2)
    def test_duplicate_time(self):
        with self.assertRaisesRegex(ValueError,'strictly increasing'):analyze_kinetics(np.array([0.,1.,1.]),np.array([3.,2.,1.]))
    def test_descending_time(self):
        with self.assertRaises(ValueError):analyze_kinetics(np.array([0.,2.,1.]),np.array([3.,2.,1.]))
    def test_mismatch(self):
        with self.assertRaises(ValueError):analyze_kinetics(self.t,self.c[:-1])
    def test_too_short(self):
        with self.assertRaises(ValueError):analyze_kinetics(np.array([0.]),np.array([1.]))
    def test_2d(self):
        with self.assertRaises(ValueError):analyze_kinetics(self.t.reshape(1,-1),self.c)
    def test_negative_concentration(self):
        with self.assertRaises(ValueError):analyze_kinetics(np.array([0.,1.]),np.array([2.,-1.]))
    def test_nonfinite(self):
        with self.assertRaises(ValueError):analyze_kinetics(np.array([0.,float('nan')]),np.array([2.,1.]))
    def test_wrong_type(self):
        with self.assertRaises(TypeError):analyze_kinetics([0.,1.],np.array([2.,1.]))
    def test_complex_rejected(self):
        with self.assertRaises(TypeError):analyze_kinetics(np.array([0+0j,1+0j]),np.array([2.,1.]))
    def test_increasing_concentration_negative_consumption_rate(self):
        r=calculate_interval_rates(np.array([0.,1.]),np.array([1.,2.]))
        self.assertAlmostEqual(r[0],-1.)
if __name__=='__main__': unittest.main()
