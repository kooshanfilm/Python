class Duck():

    def quack(self):
        print('Quaaack')

    def walk(self):
        print('walk like a duck')

    def bark(self):
        print('duck can not bark')

    def fur(self):
        print('duck has fur')


class Dog():
    def quack(self):
        print('bark')

    def walk(self):
        print('walk like a dog')

    def bark(self):
        print('dog can not bark')

    def fur(self):
        print('dog has fur')


def main():
    donold = Duck()
    fido = Dog()
    in_the_forest(donold)

def in_the_forest(dog):
    dog.bark()
    dog.fur()


def in_the_pond(duck):
    duck.quack()
    duck.walk

    # don't care which class has which method
    # for o in (donold, fido):
    #     o.quack()
    #     o.walk()
    #     o.fur()




if __name__ == '__main__': main()
