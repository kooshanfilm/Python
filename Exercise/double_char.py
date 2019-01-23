# Given a string, return a string where for every char in the original, there are two chars.


def double_char(str):

    temp_char = ''
    for letter in str:
        temp_char += letter * 2

    return temp_char

print (double_char('kou'))
