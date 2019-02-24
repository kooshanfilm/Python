#
#
# Implement a function that takes as input three variables,
# and returns the largest of the three. Do this without using the Python max() function!
#
# The goal of this exercise is to think about some internals that Python normally takes
# care of for us. All you need is some variables and if statements!


def max_number(num1,num2,num3):

    temp = 0
    if num1 >= num2:
        temp = num1
    else:
        temp = num2

    if temp >= num3:
        print "max is {} ".format(temp)
    else:
        print "max is {}".format(num3)


max_number(1,6,3)