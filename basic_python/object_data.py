
class Duck:


    def __init__(self,**kwargs):

        self._color = kwargs.get('color','white')


    def quack(self):
        print('Quaaack')

    def walk(self):
        print('walk like a duck')

    def set_color(self,color):
        self._color = color

    def get_color(self):
        return self._color

    def set_variable(self,k,v):
        self.variable[k] = v

    def get_variable(self,k):
        return self.get_variable(k,None)


def main():
    donald = Duck(color='blue')
    print(donald.get_color())

if __name__ == '__main__': main()
