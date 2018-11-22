import unittest
import dice

class DieTest(unittest.TestCase):
    def setUp(self):
        self.d6 = dice.Die(6)
        self.d8 = dice.Die(8)

    def test_add(self):
        self.assertIsInstance(self.d6+self.d8,int)

if __name__ == '__main__':
    unittest.main()