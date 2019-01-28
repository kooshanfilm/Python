#
#
# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.




def less_than_ten(a):
    new_list = []
    for numbers in a:
        if numbers < 5:
            new_list.append(numbers)
    return new_list


print (less_than_ten([1, 1, 1, 3, 5, 8, 13, 21, 34, 55, 89]))