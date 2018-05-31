import unittest
import calc

class TestCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(15, calc.add(5,10))
		self.assertEqual(9, calc.add(-1,10))
		self.assertEqual(-4, calc.add(-2,-2))

	def test_substract(self):
		self.assertEqual(5, calc.substract(10,5))
		self.assertEqual(-11, calc.substract(-1,10))
		self.assertEqual(0, calc.substract(-2,-2))

	def test_multiply(self):
		self.assertEqual(50, calc.multiply(5,10))
		self.assertEqual(-10, calc.multiply(-1,10))
		self.assertEqual(4, calc.multiply(-2,-2))

	def test_divide(self):
		self.assertEqual(0.5, calc.divide(5,10))
		self.assertEqual(-0.1, calc.divide(-1,10))
		self.assertEqual(1, calc.divide(-2,-2))
		self.assertEqual(2.5, calc.divide(5,2))

	def test_divide_by_zere(self):
		with self.assertRaises(ValueError):
			calc.divide(10,0)

if __name__ == '__main__':
	unittest.main()

