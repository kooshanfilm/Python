

# Find the first non-repeating character in given string


def find_str(word):

    my_list = []
    second_list = []
    for i in word:
        my_list.append(i)



    for char in my_list:
        if char in second_list:
            print "",
        else:
            second_list.append(char)

    print list(my_list) - list(second_list)

find_str("abcabcdef")