# Calculate the frequency of characters in a string. 
# Print each char with its frequency. e.g. For input <abcabc>, output should be <(a,2),(b,2),(c,2)>.


def numberOfFreq(mstring):
	frequcnyd = {}
	count = 1
	for i in mstring:
		if i in frequcnyd:
			frequcnyd[i]+=1

		else:
			frequcnyd[i] = count 


	print (frequcnyd)



numberOfFreq("abcabca")			



