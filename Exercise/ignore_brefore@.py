

# abcd.yaht@yahoo.com >> abcd@yahoo.com

def myword(word):
    char = word.index("@")
    char2 = word.index(".")
    x = 0
    new_list = []
    sec_list = []
    while x < char2:
        new_list.append(word[x])
        x +=1

    while char < len(word):
        sec_list.append(word[char])
        char+=1

    return "".join(new_list) + "".join(sec_list)

print myword("abcd.yaht@yahoo.com")

