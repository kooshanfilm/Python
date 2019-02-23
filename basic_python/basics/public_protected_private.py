

class Car:
    color = "blue"
    _year = 1980 # protected attribute
    __madein = "Japan"

class Bmw(Car):
    def __init__(self):
        print ("the color of car {}".format(self.color))
        print ("the year the car made {}".format(self._year))
        print ("car made in {}".format(self.__madein))



car = Car()
bmw = Bmw()


