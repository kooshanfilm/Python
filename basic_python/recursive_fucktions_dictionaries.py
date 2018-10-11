

eventDic = {'fname':'james',
			 'lname':'wood'}

print ("your name",eventDic['fname'])
eventDic['city'] = 'woodland'
print('city' in eventDic)
print(eventDic.values())

print("loop")
for k,v in eventDic.items():
	print(k,v)

# print("delete------>")
# del eventDic['fname']
# print(eventDic.values())

print("now input")
employee = []
Fname,Lname =input("enter Employee name:").split()
employee.append({'Fname':Fname,'Lname':Lname})

print(employee)
