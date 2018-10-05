


def fun():
	yield 1
	yield 2
	yield 3



print (type(fun()))


def fun2():
	i = 1
	while i <= 4:
		yield i * 2
		print("now i = {}".format(i))
		i+=1

call = fun2()

print(call.next())
print(call.next())
print(call.next())
print(call.next())

