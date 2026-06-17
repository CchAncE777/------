import unittest
from formula import Math_Y

class TestFormula(unittest.TestCase):
    def setUp(self):
        self.M_1 = Math_Y(1, 2, 3)
        self.M_2 = Math_Y(0, 2, 1)

    def test_past_formula_1_nice(self):
        self.assertEqual(self.M_1.check_log(), 0.0)

    def test_past_formula_2_nice(self):
        self.assertEqual(self.M_1.check_delit(), 1.0)

    def test_past_formula_1_no_nice(self):
        self.assertRaises(ValueError, self.M_2.check_log)

    def test_past_formula_2_no_nice(self):
        self.assertRaises(ZeroDivisionError, self.M_2.check_delit)

    def test_correct_input(self):
        self.assertRaises(TypeError, Math_Y, 'cekp', 1, 2)