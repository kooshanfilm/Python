


import unittest

from arr_rev import *


class Mytest(unittest.TestCase):

    def test_reverse_mee(self):
        self.assertEqual(reverse_mee("abc"),"c")


if __name__ == '__main__':
    unittest.main()
