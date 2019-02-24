# Given a sentence, reverse all the words in that sentence.
# Eg. I/P : This is sample text
# O/P : sihT si elpmas txet


def reverseWords(sent):

    sent_in_arr =  (sent.split())
    # print(sent_in_arr)

    i = len(sent_in_arr[0])
    for i in range(0,len(sent_in_arr)):
        first = sent_in_arr[i]
        while i > 0:
            print (first[i-1],end="")
            i-=1






reverseWords("This is sample text")
