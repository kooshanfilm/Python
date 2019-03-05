
'''

Given a list of numbers, write a Python program to find the sum of all the elements in the list.

Input: [12, 15, 3, 10]
Output: 40

'''


def find_sum(mylist):
    sum = 0
    for i in range(0,len(mylist)):
        sum  = mylist[i] +sum

    print (sum)
find_sum([10, 10, 3, 10])