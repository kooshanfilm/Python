# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

#3*2*1

# def find_fact(num):
#     if num <=1:
#         return 1
#     else:
#         result = num * find_fact(num-1)
#         return result
# print(find_fact(3))

# by look
# 4x3x2x1

def fact(num):
    f = 1
    for i in range(1,num+1):
        f = f * i

    return f

print fact(4)