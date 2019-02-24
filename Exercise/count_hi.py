# Return the number of times that the string "hi"
# appears anywhere in the given string.
#

# hi james hi
def count_hi(str):

    l = len(str)
    i = 0
    count = 0
    while i < l :
        if str[i] == 'h' and str[i+1] =='i':
            count+=1
        i+=1
    return count


print (count_hi('hihi koushan hi'))