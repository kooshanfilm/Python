
import unittest

# [1,4,6] >> 1

def min_arr(my_list):

    min = my_list[0] #1
    for i in my_list:
        if i < min:
            min = i
    return min

class Find_min(unittest.TestCase):

    def test_min_arr(self):

        self.assertEqual(min_arr([5,41,83,29]),5)
        self.assertEqual(min_arr([3,6,1,5]),1 )
        self.assertEqual(min_arr([2,90]), 2)
        self.assertEqual(min_arr([1, 3.14159,-2.71828]),-2.71828 )

if __name__ == '__main__':
    unittest.main()