#
#
# Write a Python program to count the number of characters (character frequency)
# in a string. Go to the editor Sample String :
# google.com' Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


def num_char(str):

    count = 0
    dic = {}
    for i in str:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
    print dic


num_char("google.com")