class Parents():

    def last_name(self,last_name):
        self.last_name = last_name

    def print_client(self):
        print (self.last_name)


class Child(Parents):

    def test(self):
        return False


call_client = Child()
call_client.last_name("james")
call_client.print_client()