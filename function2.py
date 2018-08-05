

def main():
    func()
    func2(1)


def func():
    for i in range(2,5):
        print(i,end = ' ')
    print()

def func2(a):
    for i in range(a,10):
        print(i,end = ' ')
    print()


if __name__ == '__main__': main()

