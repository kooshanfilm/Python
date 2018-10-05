import sys
import os
import datetime


def main():
    print('python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    print(os.name)
    x= list(range(2,20))
    print(x)


    now = datetime.datetime.now()

    last_year = 2018
    last_month = 3
    last_day = 6

    now_month = now.month
    now_day = now.day

    dmonth =  now_month - last_month
    dday =  now_day -last_day

    print ( dmonth, dday)
    days = dmonth*30+dday
    print(days,'days')




if __name__ == '__main__': main()



