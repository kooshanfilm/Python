 # Write a script to print the no. of occurrences of a given character or all letters in a string.

# hey this is just a test >> t >> 4


def numberOfChar(mstr,schar):
	count = 0
	for char in mstr:
		if char == schar:
			count+=1
	print count

	

numberOfChar("hey this is just a test","t")

