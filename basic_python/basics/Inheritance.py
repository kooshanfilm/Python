class Apple():

    ceo = "Steve Jobs"
    address ="1800 infinity road"


    def about_app(self):
        print "This is apple product"
        print ("CEO {}" .format(self.address))



class Macbook(Apple):

    def macboodAir(self):
        print ("Apple product made in {}".format(self.address))
        self.about_app()



myapple = Macbook()
myapple.macboodAir()

