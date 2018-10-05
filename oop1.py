class Employee:

	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + 'last'

		Employee.num_of_emps +=1

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount = amount

	def full_name(self):
		return '{}{}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def from_string(cls,emp_str):
		firs,last,pay = emp_str_1.split('-')
		cls(first,last,pay)

	@staticmethod
	def is_workday(day):
		pass

#print(Employee.num_of_emps)
emp_1 = Employee('james','wood',1000)
#print(emp_1.first,Employee.num_of_emps)
emp_2 = Employee('test','user',5000)

new_emp_1 =


# print(emp_2.first,emp_2.last)
# print(emp_1.full_name())
# print(emp_1.pay)
print(emp_1.apply_raise())
print(emp_1.pay)
Employee.set_raise_amt(2)
print(emp_1.apply_raise())
print(emp_1.pay)
#print(emp_1.first,Employee.num_of_emps)

