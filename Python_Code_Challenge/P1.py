import random

print (" welcome to guess number ")
name = raw_input(" Tell me your name: ")
print("hello " + name)

number = random.randint(1,20)
for guess_num in range(1,6):
    guess = int(raw_input("Take a guess: "))
    if guess < number:
        print("Your number is lower than our number")
    elif guess > number:
        print("Your number is higher than our number")
    else:
        break

if guess == number:
    print ("Bingooo " + str(guess_num))
else:
    print ("You lost our number was" + number)



