
def main():

    print("this is function")
    for i in inclusive_range(0,10,1):
        print(i,end= '')


def inclusive_range(start,stop,step):
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__': main()
