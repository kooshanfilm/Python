



def main():
    func(1,2,34,5,67)

def func(this,that,other,*args):

    print('test')
    print(this,that,other,args)
    for n in args:
        print (n,end=',')

    # args is good when you don't know how many value you have for parameter


if __name__ == '__main__': main()
