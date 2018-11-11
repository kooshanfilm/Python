

class Reverse:

    # arr = [1,2,3,5]
    # new_arr = [5,4,3,2,1]


    def my_arry(self):

        my_arr = [1,2,3,4,5]

        arr_lenght = my_arr.__len__()
        while arr_lenght > 0:
            print (my_arr[arr_lenght-1],end=",")
            arr_lenght-=1


def main():
    call = Reverse()
    #call.my_arry()


if __name__ == '__main__':
    main()


import unittest

class TestReverse(Reverse):

    def test_my_arry(self):
        assert arr_lenght > 0