# 4! = 4 × 3 × 2 × 1 = 24
# x! = (x)*(x-1)*(x-2)*(x-n)


def fact_2(n):
    sum = 1
    while (n > 1):
        sum = sum * n
        n-=1

    print(sum)


def fact(n):
    sum = 0
    list = []
    while (n >= 1):
        list.append(n)
        sum = (n) * (n - 1)
        n-=1
    print(list)


    x = (n)*(n-1)*(n-2)*(n-3)
    print('x',x)

fact_2(4)
