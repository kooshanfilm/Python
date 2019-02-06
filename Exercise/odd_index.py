# Write a Python program to remove the characters which have odd index values of a given string.
#


def delete_odd(s):
    new_list = []
    for i in s:
        new_list.append(i)

    x = 0
    while x < len(new_list):
        print (new_list[x]),
        x+=2


delete_odd("abcdef")