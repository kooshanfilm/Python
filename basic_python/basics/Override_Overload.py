

class Employee:

    def setNumberOfWorkingHours(self):
        self.numberofworkinghours = 40


    def displayNumberOfWorkingHourse(self):
        print (self.numberofworkinghours)


class Traniee(Employee):

    def setNumberOfWorkingHours(self):
        self.numberofworkinghours = 45

    def resetNumberofWorkingHours(self):
        super().setNumberOfWorkingHours()


employee = Employee()
employee.setNumberOfWorkingHours()
employee.displayNumberOfWorkingHourse()
traniee = Traniee()
traniee.setNumberOfWorkingHours()
traniee.displayNumberOfWorkingHourse()
traniee.setNumberOfWorkingHours()
traniee.resetNumberofWorkingHours()
traniee.displayNumberOfWorkingHourse()
