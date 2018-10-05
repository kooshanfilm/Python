from datetime import date

import datetime

def main():
    today = datetime.date.today()
    someday = datetime.date(2017, 10, 18)
    diff =  today - someday
    month = (diff.days)

    months = month //30
    days = (month %30)
    print ('starting', months,days)


if __name__ == '__main__': main()
