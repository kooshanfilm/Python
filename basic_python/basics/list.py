
def main():
   j = 'Koushan'
   x = (1,2,3,4)
   y = [1,2,3,4]

   y.append(8) # only list you can cuz its imutable
   y.insert(0,12) #index and number

   print (type(j), j)
   print (type(x),x)
   print(type(y), y)
   print (j)
   print(j[0:2])

   for p in j:
       print(p)

if __name__ == '__main__': main()
