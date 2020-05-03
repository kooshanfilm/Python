 # Reversing string:

def stringReverse(my_string):

    # breaking down strings into small characters
    chars = list(my_string)

    # reversing array
    reverse = chars[::-1]

    # joining chars together
    str = ""
    return str.join(reverse)

print (stringReverse("ABC"))





