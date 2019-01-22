#3! = 3*2*1

def fact(num):

	if num <= 1:
		return 1
	else:
		result = num * fact(num - 1)
		return result


print (fact(4))
