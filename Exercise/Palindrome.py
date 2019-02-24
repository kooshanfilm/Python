#
# A palindrome is a word that reads the same backward or forward.
# Write a function that checks if a given word is a palindrome.
# Character case should be ignored.
# For example, is_palindrome("Deleveled") should return True as
# character case should be ignored, resulting in "" \
#  "deleveled", which is a palindrome since it reads the same backward and forward.

# @staticmethod


def is_palindrome(word):
    old_list = []
    for i in word:
        old_list.append(i)

    new_list = []
    i = 0
    str_len = len(word)
    while i < str_len:
        new_list.append(word[str_len-1])
        str_len-=1

    if old_list ==  new_list:
        print "plam"
    else:
        print "not"


is_palindrome("anna")





# print(Palindrome.is_palindrome('Deleveled'))
