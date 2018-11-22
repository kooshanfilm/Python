import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

	def test_email(self):
		emp_1 = Employee('James','wood',100)
		emp_2 = Employee('Tom','lee',200)

		self.assertEqual(emp_1.email('ames.wood@email.ccom'))




	if __name__ == '__main__':
	    unittest.main()


