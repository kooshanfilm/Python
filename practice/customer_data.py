
customers  = []

while True:
	createEntry = input("enter customer (Yes/No):")
	createEntry = createEntry[0].lower()
	if createEntry == 'n':
		break
	else:
		fName,Lname = input("first name and last: ").split()
		customers.append({'fName':fName,'Lname':Lname})

for cust in customers:
	print(cust['fName'],cust['Lname'])
