import datetime


class Cic:

    def __init__(self,t_year,t_month,t_day):
        self.t_year = t_year
        self.t_month = t_month
        self.t_day = t_day

    def app_sent(self,year,month,day):
        self.year = year
        self.t_month = month
        self.t_day = day
        return self.year,self.t_month,self.t_day

    def current_time(self):
        now = datetime.datetime.now()
        now_month = now.month
        now_day = now.day
        now_year = now.year
        return now_year,now_month,now_day

    def test_to_now(self):

        date = Cic.current_time(self)
        print('your test month was {}, and your day was {}'.format(self.t_month,self.t_day))
        dmonth = date[0] - self.t_month
        dday = date[1] - self.t_day
        total_days = (dmonth * 30) + dday
        print('{} months and {} days'.format(dmonth,dday))
        print('total days {}'.format(total_days))

    def app_to_now(self,year,month,day):

        current_time = Cic.current_time(self)

        dyear = current_time[0] - year
        dmonth = current_time[1] - month
        dday = current_time[2] - day


        print('------')
        print (dyear,'',dmonth,',',day)

def main():
    cic = Cic(2018,3,6)
    cic.test_to_now()






if __name__ == '__main__': main()
