from quickstart import *
from termcolor import colored
import time
import os
from Stock_price import *
import sys



class Market(Read_sheet):



    def __init__(self):
        self.market = Jadi()

    def read_excel_sheet(self):

        self.value = Read_sheet.reed_google(self)
        return self.value

    def decoration(self, account):
        self.account = account
        print("")
        print("***{}***".format(account))
        print("")

    def rrsp_stat(self, sum=0):
        self.sum = sum
        Market.decoration(self, 'R')
        result = self.value
        for i in range(28, 32):
            sym = result[i][0]
            sym = sym.upper()
            price = result[i][7].replace(",", "")
            price = float(price)
            self.sum = self.sum + price
            if price >= 0:
                print("------------------------------------")
                print(colored("{} is up now by {}".format(sym, price), 'green'))
                print("------------------------------------")
            else:
                print(colored("{} {}".format(sym, price), 'red'))
        print('')
        Market.total_price(self, self.sum)

    def tfsa_stat(self):
        sum = 0
        Market.decoration(self, 'T')
        result = self.value
        for i in range(20, 24):
            sym = result[i][9]
            current_stock_price = result[i][15]
            sym = sym.upper()
            price = result[i][16].replace(",", "")
            price = float(price)
            sum = sum + price
            if price > 0:
                print("------------------------------------")
                print(colored("{} is up now by {}".format(sym, price), 'green'))
                print("------------------------------------")
            else:
                # print(colored("{}---------{}----------{}".format(sym,current_stock_price, price), 'red'))
                print(colored("{}    {}".format(sym, price), 'red'))

        print('')
        Market.total_price(self,sum)
        print('__________________________________')
        Market.total_price(self,self.sum,sum)

    def total_price(self,sum1,sum2=0):
        total = sum1 + sum2
        if total > 0 :
            print(colored("Totla:{}".format(total), 'green'))
        else:
            print(colored("Totla:{}".format(total), 'red'))


    def get_result(self):

        refresh = raw_input()
        while (refresh == "y"):
            Market.read_excel_sheet(self)
            Market.rrsp_stat(self)
            Market.tfsa_stat(self)
            Market.stock_price(self)
            time.sleep(10)
            bashCommand = "clear"
            os.system(bashCommand)
            refresh = raw_input()

    def stock_price(self):
        tfsa_stock_list = ['nflx','amzn','fb','tsla']
        rsp_stock_list = ['mu','googl','fb','baba','tsla']
        self.check_current_price = Stock_price() # create instance from another class

        for stock in tfsa_stock_list:
            print (stock.upper()),
            print (self.check_current_price.check_price(stock))
        print('__________________________________')
        for stock in rsp_stock_list:
            print (stock.upper()),
            print (self.check_current_price.check_price(stock))


def main():
    call = Market()
    call.get_result()




if __name__ == '__main__':
    main()