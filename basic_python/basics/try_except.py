while True:
    try:
        user = int(input())
        if user < 0:
            raise ValueError("please give positive number")
        else:
             print("user input: %s" % user)
    except ValueError as e:
        print(e)