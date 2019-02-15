import unittest

# Find the only element that appears b times
'''
[1,2,3,2,1,4]
1 = 2
2 = 2
3 = 1
4 = 1
2 > 2
'''
def find_element(my_list,num_times):
    count = 0

    for num in my_list:
        if num  == num_times:
            count +=1
    return count


class Find_elem(unittest.TestCase):

    def test_find_element(self):
        self.assertEqual(find_element([1,2,3,2,1,4],2),2)
        self.assertEqual(find_element([1, 2, 3, 2, 1, 4], 4), 1)
        self.assertEqual(find_element([1, 2, 3, 2, 1, 4], 3),1)


if __name__ == '__main__':
    unittest.main()


