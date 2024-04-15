# python3 -m unittest .\test_logic.py
import unittest
from logic import calc_lineal, calc_quad

class TestCalcFunctions(unittest.TestCase):

    def test_calc_lineal(self):
        self.assertAlmostEqual(calc_lineal(2, 4), -2.0)  # 2x + 4 = 0 -> x = -2
        self.assertAlmostEqual(calc_lineal(3, -9), 3.0)  # 3x - 9 = 0 -> x = 3
    
    def test_calc_lineal_invalid_input(self):
        with self.assertRaises(ZeroDivisionError):
            calc_lineal(0, 0)

    def test_calc_quad(self):
        # Один корень
        self.assertListEqual(calc_quad(1, -2, 1), [1.0])  # x^2 - 2x + 1 = 0 -> x = 1
        # Два корня
        self.assertListEqual(calc_quad(1, -3, 2), [2.0, 1.0])  # x^2 - 3x + 2 = 0 -> x = 2, 1
        # Нет корней
        self.assertIsNone(calc_quad(2, 3, 5))  # 2x^2 + 3x + 5 = 0, нет корней

    def test_calc_quad_invalid_input(self):
        with self.assertRaises(ZeroDivisionError):
            calc_quad(0, 0, 0)
