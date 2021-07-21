import unittest
from calculadora import Calculadora

#C:\Users\lfochtman\Documents\01\Python>python -m unittest discover

class TestBasicos(unittest.TestCase):

	def test_una_calculadora_nueva_inicia_en_cero(self):
		cal=Calculadora()
		self.assertEqual(0,cal.valor())

	def test_suma_2_mas_3(self):
		cal=Calculadora()
		cal.suma([2,3])
		self.assertEqual(5,cal.valor())

	def test_suma_n_nros(self):
		cal=Calculadora()
		cal.suma([4,5,2])
		self.assertEqual(11,cal.valor())

	def test_producto_n_nros(self):
		cal=Calculadora()
		cal.producto([4,5,2])
		self.assertEqual(40,cal.valor())

	def test_divide_2_nros(self):
		cal=Calculadora()
		cal.division(5,2)
		self.assertEqual(2.5,cal.valor())

	def test_resta_2_nros(self):
		cal=Calculadora()
		cal.resta(1,3)
		self.assertEqual(-2,cal.valor())
