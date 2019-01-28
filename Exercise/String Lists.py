#
#
# # Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)



# def palindrom_or_not(a):
#     i = 0
#     new_list = []
#     string_leng = len(a)
#     for i in a:
#         new_list.append(a[string_leng-1])
#         string_leng-=1
#     print new_list
#     if a == new_list:
#         print "yes"
#
#
# palindrom_or_not("ccc")

wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
