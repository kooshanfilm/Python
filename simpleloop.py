

class Fib():


    def __init__(self,a,b): #constroctor
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a,self.b = self.b,self.a + self.b

f = Fib(0,1)  #constractor
for r in f.series():
        if r > 100 :
            break
        print(r)