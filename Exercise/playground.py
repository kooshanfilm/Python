# Write a Python program to calculate the sum of a list of numbers


def sum_list(lis):
    sum = 0
    for i in lis:
        sum = sum + sum_list(lis)

    print sum


sum_list([1,2,3])