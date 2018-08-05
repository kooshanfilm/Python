

def main():
    a , b = 1,1

    if a < b :
        print(a,"a is less than B",b)
    else:
        print(a,"is greater than B",b)

#OR

    if a < b:
        print(a, "a is less than B", b)
    elif a > b:
        print(a, "is greater than B", b)
    else:
        print ("a is equal to be")

#OR

    s = "less than " if  a < b else "a not less than"
    print(s)




if __name__ == '__main__':
    main()
