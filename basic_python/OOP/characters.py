import random

class Character:

    def __init__(self,name,**kwargs):
        self.name = name

        for key,value in kwargs.items():
            setattr(self,key,value)
    def __str__(self):
        return "{}:{}".format(self.__class__.__name__,self.name)

# inheret from the character class
class Thief(Character):

    # can define atribute in the class
    sneaky = False

    def __init__(self,name,sneaky=True,**kwargs):
        super().__init__(name,**kwargs )
        self.sneaky = sneaky


    # def __init__(self,name,sneaky=True,**kwargs):
    #     self.name = name
    #     self.sneaky = sneaky
    #
    #     for key,value in kwargs.items():
    #         setattr(self,key,value)

    def pickpocket(self):
        # if self.sneaky:
        #     #print("called by {}".format(self))
        #     return bool(random.randint(0,1))
        # else:
        #     return False
        return self.sneaky and bool(random.randint(0,1))

    def hide(self,light_level):
        return self.sneaky and light_level < 10

    def what_do_i_have(self):
        print (self.name,self.sneaky)


def main():
    call = Thief("james",scars = None,fav_name="woody")
    call2 = Character("mike")
    #print(call.pickpocket())
    # print (call.hide(4))
    # call.what_do_i_have()
    # print (call.fav_name)
    call.what_do_i_have()
    print(call.__str__())
    print(call2.__str__())
    




if __name__ == '__main__':
    main()