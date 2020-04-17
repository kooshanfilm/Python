import random

theasurus = {
    "weather" : ['balmy', 'summery','hot','cold'],
    "cold" : ['a', 'b','c','d'],
    'happy': ['e','f','g','h'],
    'sad':['s','a','d','d2']
}
print ("Welcome to my app")
print ("\n Choose a word from our list")
print ("\n Here are words for you")

for key in theasurus.keys():
    print ("\t - " + key)

choice = raw_input("\n  What world would you like to get: ").lower().strip()

if choice in theasurus.keys():
    index = random.randint(0,4)
    print(" Your random word is " +  theasurus[choice][index])

else:
    print("Sorry not here")

choice = raw_input(" Would you like to see everything: ").lower().strip()

if choice == "yes":
    for key,value in theasurus.items():
        print(key.title())




