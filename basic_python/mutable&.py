def main():


    x = 42
    print((id(x)))
    y = 42
    print((id(y)))
    print(x==y)
    print(x is y)

    x2 = dict(x = 42)
    print (type(x2))
    print((id(x2)))

    y2 = dict(y=42)
    print(type(y2))
    print((id(y2)))

    print(x2 == y2)


if __name__ == '__main__': main()
