import unittest

def missing_element(f_list,s_list):

    missing_arr = []
    for i in f_list:
        if i in s_list:
            pass
        else:
            missing_arr.append(i)
    missing = missing_arr[0]
    return missing

class Missing_elements(unittest.TestCase):

    def test_missing_element(self):
        self.assertEqual(missing_element([4,5,9],[4,5,9]),8)
        self.assertEqual(missing_element([4, 5, 8, 9], [4, 5, 9,8]), )

if __name__ == '__main__':
    unittest.main()
