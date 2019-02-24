

# Write a Python program to convert a string in a list.

def string_list(str):
    new_list = []
    for i in str:
        new_list.append(i)

    print new_list

    print str.split()



string_list("abcd hello hello")