

class numstring:
    def __init__(self,value):
        self.value = str(value)


    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

def main():
    call = numstring(5)
    print((call.__str__()),type(call.__str__()))
    print((call.__int__()))
    print((call.__float__()))



if __name__ == '__main__':
    main()