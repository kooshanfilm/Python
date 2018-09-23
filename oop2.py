

class Person:


    count = 0
    def __init__(self,name):
        print("object created")
        self.name = name
        self.birth = '12,3,4,'
        Person.count += 1
        print (name + ' created')

    def func(self,name):
        print(name)


def main():
    obj1 = Person('james')
    #james = Person('james')
    #marry = Person('mary')


if __name__ == '__main__': main()



