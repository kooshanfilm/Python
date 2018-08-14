



def main():
    func(3,4,5,6,67,one = 1,two = 2,three =3)

def func(*args,**kwargs):
    print(kwargs)
    print(kwargs['one'],kwargs['two'],args)



if __name__ == '__main__': main()
