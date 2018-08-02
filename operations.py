


def main():
    a , b = 1,2
    c , d = 4,5

    print (type(a))

    print(a,b)

    print(c, d)

    c , d = d,c

    print(c, d)

    f = (1,2,3,4,5)

    print (type(f),f)

    g = [1,2,3,4,5]
    print(type(g), g)



if __name__ == '__main__':main()


# <class 'int'>
# 1 2
# 4 5
# 5 4
# <class 'tuple'> (1, 2, 3, 4, 5)
# <class 'list'> [1, 2, 3, 4, 5]