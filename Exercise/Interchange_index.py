
import unittest

# Python program to interchange first and last elements in a list
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]


def interchange(my_list):
    # temp_front = my_list[0]
    # temp_back = my_list[-1]
    # my_list[0] = temp_back
    # my_list[-1] = temp_front
    #
    my_list[0], my_list[-1] = my_list[-1],my_list[0]

    return my_list

# interchange([12, 35, 9, 56, 24])

class test_interchange(unittest.TestCase):

    def test_interchange(self):
        self.assertEqual(interchange([12, 35, 9, 56, 24]),[24, 35, 9, 56, 12])

unittest.main()