class Animal:
    def talk(self):
        print('I talk')

    def walk(self):
        print('I walk')

    def clothes(self):
        print('this is clothes>> animal class')


class Duck(Animal):

    def quack(self):
        print('Quaaack')

    def walk(self):
        print('walk like a duck')

    def clothes(self):
        super().clothes()
        print('print my clothes<<< Duck')


class Dog(Animal):
    def clothes(self):
        # print ('fido in dog class')
        pass


def main():
    fido = Dog()
    fido.clothes()


if __name__ == '__main__': main()
