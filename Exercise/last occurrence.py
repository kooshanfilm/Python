

# Write a Python program to split a string on the last occurrence of the delimiter.


def last_occurance(word,position):
    new_list =[]
    for i in word:
        new_list.append(i)

    new_list.insert(3,"X")

    for char in new_list:
        print char,







last_occurance("ABCD",3)