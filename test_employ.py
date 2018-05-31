import unittest
from employ import Employ
from unittest.mock import patch

class Test_Employ(unittest.TestCase):
	
	def setUp(self):
		print('setUp')
		self.emp_1 = Employ('Pepe', 'Perez', 50000)
		self.emp_2 = Employ('Luis', 'Manzorro', 20000)
	
	def tearDown(self):
		print('tearDown')
		pass

	def test_email(self):
		print('test_email')
		self.assertEqual(self.emp_1.email, 'Pepe.Perez@example.com')
		self.assertEqual(self.emp_2.email, 'Luis.Manzorro@example.com')

		self.emp_1.first = "Manuel"
		self.emp_2.first = "Antonio"

		self.assertEqual(self.emp_1.email, 'Manuel.Perez@example.com')
		self.assertEqual(self.emp_2.email, 'Antonio.Manzorro@example.com')

	def test_fullname(self):
		print('test_fullname')
		self.assertEqual(self.emp_1.fullname, 'Pepe Perez')
		self.assertEqual(self.emp_2.fullname, 'Luis Manzorro')

		self.emp_1.first = "Manuel"
		self.emp_2.first = "Antonio"
		
		self.assertEqual(self.emp_1.fullname, 'Manuel Perez')
		self.assertEqual(self.emp_2.fullname, 'Antonio Manzorro')

	def test_apply_raise(self):
		print('test_apply_raise')
		self.emp_1.apply_raises()
		self.emp_2.apply_raises()

		self.assertEqual(52500, self.emp_1.pay)
		self.assertEqual(21000, self.emp_2.pay)

	def test_monthly_schedule_success(self):
		with patch('employ.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.emp_1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Perez/May')
			self.assertTrue('Success', schedule)
	
	@patch('employ.requests.get')
	def test_monthly_schedule_fail(self, mocked_get):
			
			mocked_get.return_value.ok = False

			schedule = self.emp_1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Perez/May')
			self.assertTrue('Bad Response!', schedule)


if __name__ == '__main__':
	unittest.main()