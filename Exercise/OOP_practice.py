class Circule:
    pi = 2.14

    def __init__(self, r=1):
        self.r = r

    def calc_area(self):
        return (self.r ** 2) * Circule.pi

    def set_r(self, new_r):
        self.r = new_r


# def main():
#     c = Circule(r=5)
#     print(c.calc_area())
#     c.set_r(10)
#     print(c.calc_area())
#
#
# if __name__ == '__main__':
#     main()


class Animal:

    def __init__(self):
        print ("animal created")

    def who_am_i(self):
        print("Animal")

    def eat(self):
        print("eating")

class Dog(Animal):

    def __int__(self):
        print("Dog Created")
        Animal.__init(self)


    def who_am_i(self):
        print("Dog")

    def bark(self):
        print("Bark")

# d = Dog()
# d.eat()


class Book(object):

    def __init__(self,title,author,pages):

        print ("a book has created")
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return ("this is title {x} and author {t} and pages{y}".format(x= self.title,y = self.author,t=self.pages))

# my_book = Book('AWS','james',100)
# print (my_book.__str__())
#


class Handle:

    # try:
    #    2 + 'S'
    # except TypeError:
    #     print("there was type error")
    #
    # finally:
    #     print("FINALY - this was printed")


    # try:
    #     f = open('koushan.txt','w')
    #     f.write('\n this is just a test \n')
    # except:
    #     print("Can't write into the file")
    #
    # else:
    #     print("done wrote something ")
    #

    try:
        val = int(input("please enter something"))
    except:
        print("looks like you didn't enter corrct number")
        val = int(input("please enter again"))

    finally:
        print("finaly im here")

    print (val)

