#python esentials:

'''

remove items
new_colors = ["r","g","b","y"]

print(new_colors)
new_colors.pop()
print(new_colors)

new_colors = ["r","g","b","y"]
del (new_colors[0])

print(new_colors)


#Sorting List: Mutable == changeable
	
new_numbers= ['4','3','2','1']

# temp sorting 
print(sorted(new_numbers))
print(new_numbers)

#printng len of the function
print(len(new_numbers))

#perminat sorting
new_numbers.sort()
print(new_numbers)


#Tooples: Unmutable == not change able 

grades = [1,2,3,4,5,6]
scores = (2,3,4,5,6)

print(type(grades),grades)
print(type(scores),scores)

scores = (20,3,4,5,6)
print(scores)

#challege 1

print("welcome to the challenge")

grades = []
grade = int(input("what is your first grade 0 -100"))
grades.append(grade)

grade = int(input("\nwhat is your first grade 0 -100"))
grades.append(grade)

#sorint from highest to lowest


print("\nYour grades are:", str(grades))
'''
print ('welcome to binary/hexadecimal converter app')
#Get user input
max_value = input("\nCompute binary")
decimal = list(range(1, max_value + 1))
binary = []
hexdecimal = []
for num in decimal:
    binary.append(bin(num))
    hexdecimal.append((hex(num)))

low_range = input("\nyour low range")
high_range = input("\n high range")
for num in decimal[low_range - 1:high_range]:
    print (num)


