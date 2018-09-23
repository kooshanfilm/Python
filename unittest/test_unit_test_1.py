
import unittest
import unit_test_1


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = unit_test_1.add(10,5)
        self.assertEqual(result,15)




if __name__ == '__main__':
    unittest.main()

