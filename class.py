class Nedah:

    def __init__(self,kind = "girl"):
        self.kind = kind

    def whatkind(self):
        return self.kind

def main():
    girl = Nedah() # got the parameter from constractor
    nice_girl = Nedah("nice")

    print(girl.whatkind())
    print(nice_girl.whatkind())

if __name__ == '__main__': main()



