#Find first and last positions of an element in a sorted array
# Input : arr[] = {1, 3, 5, 5, 5, 5 ,67, 123, 125}    
#         x = 5
# Output : First Occurrence = 2
#          Last Occurrence = 5



def first_last(mylist):
	
	arr_list = len(mylist)
	for i in range(0,arr_list-1):
		if mylist[i] == mylist[i+1]:
			num = mylist[i]
			print mylist.index(num)



first_last([1, 3, 5, 5, 5, 5 ,67, 123, 125])
