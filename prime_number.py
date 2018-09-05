class Practicing:

    def loop(self):
        for i in ['dog','cat',5]:
            print("object")
            print(i)
            print("-----")

    def squre(self):
        for i in range(1,8):
            print(i,i*i)
            print("-----")
    def name(self):
        for name in ("james","cat","tom"):
            print("Hi "+name)

    def prime_test(self,n):

        prime = True

        for i in range(2,n):
            if n % i == 0:
                prime = False
        return prime

    def count_prime(self,number):

        prime_count = 0
        last_prime_number = 0
        for i in range(1,number):
            if Practicing.prime_test(self,i):
                #print(i,Practicing.prime_test(self,i))
                last_prime_number = i
                prime_count = prime_count + 1
        print("Number of prime in range of ","2 to",number,"is", prime_count)
        print("Last prime number is " , last_prime_number)

    def array_p(self):



def main():
    jadi = Practicing()
    #jadi.loop()
    #jadi.squre()
    #jadi.name()
    #print (jadi.prime_test(10))
    #jadi.count_prime(4)




if __name__ == '__main__':main()

