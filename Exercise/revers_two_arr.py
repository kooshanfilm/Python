import unittest


# [1,4,5,6,3,9] >> [1,4,5] [6,3,9] >> [5,4,1] [9,3,6]

def reverseTwoArr(mylist):
    arr_l = len(mylist)  # 6
    two_arr = int((arr_l) / 2)  # 3
    first_arr = mylist[:3]
    sec_ar = mylist[3:]

    i = 0
    first_arr_l = len(first_arr)

    return reverse(first_arr), reverse(sec_ar)


def reverse(anylist):
    i = 0
    anylist_l = len(anylist)
    another_list = []
    while i < anylist_l:
        another_list.append(anylist[anylist_l - 1])
        anylist_l -= 1
    return another_list


# reverseTwoArr([1,4,5,6,3,9])

class reverse_arr(unittest.TestCase):

    def test_reverseTwoArr(self):
        self.assertEqual(reverseTwoArr([1, 4, 5, 6, 3, 9]), ([5, 4, 1], [9, 3, 6]))
        self.assertEqual(reverseTwoArr([1, 4, 5]), ([5, 4, 1], []))


unittest.main()
