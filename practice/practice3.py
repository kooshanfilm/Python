
import _random
import sys


ans = True

while ans:
    quest = input("between 1 to 5,exit enter")
    answere = _random.randint(1,5)
    if quest == "":
        sys.exit()
    elif quest == 1:
        print ("1")
    elif quest == 2:
        print("2")
    elif quest == 3:
        print("3")
    elif quest == 3:
        print("3")
    else:
        print("sry")
