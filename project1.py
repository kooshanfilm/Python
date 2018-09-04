# If we list all the natural numbers
# below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
#
# Find the sum of all the multiples of 3 or 5
# below 1000.


class Practicing:

    def multipler(self,number):
        sum_of_mult = 0
        for i in range(2,number):
            #print (i, number)
            if (i % 5) == 0 or (i % 3 ) == 0:
                print(i,end=",")
                sum_of_mult = i + sum_of_mult
        print("-----")
        print("Sum of total number",sum_of_mult)



def main():
    jadi = Practicing()
    jadi.multipler(1000)




if __name__ == '__main__':main()