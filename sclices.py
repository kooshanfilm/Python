

def main():

   list = [1,2,3,4,5]
   print (list[0])

   print(list[1:3])
   print (range(0,2))
   for i in (range(1,4)):
       print(i)

   list[:] = range(0,50)
   print (list)
   print(list[10:20:3])




if __name__ == '__main__': main()
