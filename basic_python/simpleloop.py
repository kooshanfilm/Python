

class Fib():


    def __init__(self,a,b): #constroctor
        self.a = a
        self.b = b

    def series(self):
        print(self.a,self.b)
        while(True):
            yield(self.b)
            self.a,self.b = self.b,self.a + self.b

def main():
    f = Fib(0,1)  #constractor
    for r in f.series():
            if r > 10 :
                break
            print(r)

if __name__ == '__main__':main()
