import unittest

# find commen alpha:

'''String and 
   Strong'''

def findCommon(str1,str2):

	common = []
	for char in str1:
		if char in str2:
			common.append(char)

	return "".join(common)
findCommon("string","strong")


class Findcommon(unittest.TestCase):

	def test_findCommon(self):
		self.assertEqual(findCommon("string","strong"),"strng")
		self.assertEqual(findCommon("xlx","strong"),"")
		self.assertEqual(findCommon("pppppc","sccccc"),"c")

unittest.main()


