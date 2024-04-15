# python3 -m unittest .\test_logic.py
import unittest
import logic

class Test_calc_lineal(unittest.TestCase):

    def test_lineal(self):
        self.assertEqual(logic.calc_lineal(1,5),-5)
        self.assertEqual(logic.calc_lineal(512,0),0)
        self.assertEqual(logic.calc_lineal(10,-73),7.3)

    def test_values(self):
        self.assertRaises(ValueError,logic.calc_quad,0,1,1)