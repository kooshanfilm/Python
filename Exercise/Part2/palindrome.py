

# input = "abc"
#
# input_l = len(input)
# i = 0
# new_list= []
# while i < input_l:
#     new_list.append(input[input_l-1])
#     input_l -=1
#
# if input == new_list:
#     print ("yest")

def checkPalindrome(inputString):
    reverseString = inputString[::-1]

    if(inputString == reverseString):
        return True
    else:
        return False
