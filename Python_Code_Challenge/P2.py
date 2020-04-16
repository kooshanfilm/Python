
print(" Welcome to grade sorter app ")

grades = []
grade = int(raw_input(" What is you first grade (0 - 100) "))
grades.append(grade)
grade = int(raw_input(" What is you second grade (0 - 100) "))
grades.append(grade)
grade = int(raw_input(" What is you third grade (0 - 100) "))
grades.append(grade)
grade = int(raw_input(" What is you fourth grade (0 - 100) "))
grades.append(grade)

print ("Your grades are: " + str(grades))

#Sort the list from highest to lowest
grades.sort(reverse=True)
print("Your grades from highest to lowest are" + str(grades))

#Removing the lowest two grades
print("The lowset two grades will now be dropped")
removed_grade = grades.pop()
print ("Removed grade is " + str(removed_grade))

removed_grade = grades.pop()
print ("Removed grade is " + str(removed_grade))

print("Now your grades are" + str(grades))
print ("Your highest grade is " + str(grades[0]))



