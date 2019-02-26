 # Given are two ordered lists of size 7 and 3. The first list has three vacant spots in the end. Merge them in a sorted manner with minimum no. of steps.

 # [1,2,3,4,5,6,7,,,],[8,9,0] >> [1,2,3,4,5,6,7,8,9,0]

def mergeTwo(flist,slist):
	tlist = sorted((flist + slist))
	print tlist


mergeTwo([8,7,6,5,4,0],[11,10,9]) 