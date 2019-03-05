
import unittest
import unit_test_1


class TestCalc(unittest.TestCase):

    def test_add(self):
        #self.assertEqual(unit_test_1.add(10,5),15)
        self.assertEqual(unit_test_1.add(1,0), 1)
        self.assertEqual(unit_test_1.add(-1,-1),-2)


    def test_subtract(self):
    	self.assertEqual(unit_test_1.subtract(-1,-1),0)


    def test_divide(self):
    	self.assertEqual(unit_test_1.divide(10,5),2)
    	#self.assertRaises(ValueError,unit_test_1.divide,10,0)
    	with self.assertRaises(ValueError):
    		unit_test_1.divide(10,0)
if __name__ == '__main__':
    unittest.main()

