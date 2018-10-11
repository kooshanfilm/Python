class Dog:

    def __init__(self,height="0", weight="0"):
        self.height = height
        self.weight = weight

    @property
    def height(self):
        print("Retrieving the height")

        # Put a __ before this private field
        return self.__height

    # @height.setter
    # def height(self,value):
    #     if value.isdigit():
    #         self.__height = value
    #     else:
    #         print("Please onlye enter number for height")



    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eat".format(self.name))

    def bark(self):
        print("{} the dog bark".format(self.height))

def main():
    def main():
        aSquare = Square()
        aSquare.height = 23
        aSquare.bark()





if __name__ == '__main__': main()