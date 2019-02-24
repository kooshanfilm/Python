

# Write a Python program to count and display the vowels of a given text.


def find_vowels(str):
    new_srting = []
    for i in str:
        if i == "o" or i == "e":
            new_srting.append(i)

    print new_srting


find_vowels("w3resource")
