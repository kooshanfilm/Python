
def reverse_mee(word):

    i = 0
    lenght = len(word)
    new_str = []
    while i < lenght:
        lenght -= 1
        new_str.append(word[lenght])
    return "".join(new_str)
