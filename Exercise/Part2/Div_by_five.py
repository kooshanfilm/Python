input_list = [1,2,3,4,5]

def divis_by_five(num):
	if num % 5 == 0:
		return True
	else:
		return False


xyz = (i for i in input_list if divis_by_five(i))
for i in xyz:
	print i

# div_list = []

# for i in input_list:
# 	if divis_by_five(i):
# 		div_list.append(i)

# print xyz




