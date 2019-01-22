#
# Given a string and a non-negative int n,
# return a larger string that is n copies of the original string.
#


def string_times(str, n):
    if n < 0:
        return ("Please enter positive number")

    else:
        return (str * n)



print (string_times("hi",2))