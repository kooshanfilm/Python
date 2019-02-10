import unittest

# Given an array length 1 or more of ints,
#  return the difference between the largest and smallest values in the array. Note:
# the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

# big_diff([10, 3, 5, 6])  7
# big_diff([7, 2, 10, 9])  8
# big_diff([2, 10, 7, 2])  8


def big_diff(num):
    diff_two = max(num) - min(num)
    return diff_two

# print big_diff([12,3,1,2])

class BigDiff(unittest.TestCase):

    def test_big_diff(self):
        self.assertEqual(big_diff([12,3,1,2]),11)



if __name__ == '__main__':
    unittest.main()