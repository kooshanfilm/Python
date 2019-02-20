import unittest


# [1,2,3,4,2,6,3]
# [1,2,2,3,3,4,6]

def find_duplicate(my_arr):

    sorted_arr = sorted(my_arr)
    duplicate_list = []
    for i in sorted_arr:
        if i in duplicate_list:
            sorted_arr.pop()
        else:
            duplicate_list.append(i)

    print duplicate_list



find_duplicate([1, 2, 3, 4, 2, 6, 3])

# class FindMyDuplicate(unittest.TestCase):
#
#     def test_find_duplicate(self):
#         self.assertEqual(find_duplicate([1, 2, 3, 4, 2, 6, 3]),[2,2,6])
#
#
# if __name__ == '__main__':
#     unittest.main()
