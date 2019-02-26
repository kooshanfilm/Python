

import unittest

def findMinNumber(my_list):
    sorted_list = sorted(my_list)
    sum = 0
    for i in my_list:
        sum = i + sum
    # print sum
    if sum % 2 != 0:
        return 0
    else:
        for i in sorted_list:
            # print i , sum
            if ((sum - i) % 2 !=0):
                pass
            return i

# print findMinNumber([100,23,45,21,65])

class FindSmallNumber(unittest.TestCase):

    def test_findMinNumber(self):
        self.assertEqual(findMinNumber([100,23,45,21,65]),21)


if __name__ == "__main__":
    unittest.main()



