

class Human:

    def __init__(self):
        self.name = "james"
        self.numbers = (1,2,3,4)


    def whats_my_name(self):
        print (self.name)


    @classmethod
    def go_to_school(cls):
        print ("im {}".format(cls))

    @staticmethod
    def not_go_to_school():
        print("im a static def")

    @staticmethod
    def franchise(store):

        return store

my_human = Human()
my_human.go_to_school()
my_human.not_go_to_school()

#inherat:

class Bighuman(Human):
    def __init__(self,name):
        super().__init__()
        self.name = name