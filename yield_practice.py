


def compare(n):
    if n > 10 :
        print (n," n is greater than 10")

    else:
        print(n, "is not greater than 10")
        return True


#for n in range(8,12):
 #   compare(n)


def compare2(x):
    while (True):
        if x < 10 : yield x # do this else
        print (x)
        x+= 1

compare2(7)