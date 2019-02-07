

# Write a Python program to reverse words in a string.

def reverse_me(str):

    in_aary =  str.split()
    length = len(in_aary)
    i = 0
    while i < length:
        print in_aary[length - 1] ,
        length-=1

reverse_me("python is powerfull")