import unittest


class TestMove(unittest.TestCase):
    def setUp(self):
        print("runs before each test \n")
    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        assert not 1 + 1 == 3



if __name__ == '__main__':
    unittest.main()