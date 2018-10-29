from quickstart import *
from flask import Flask, jsonify, Response
from flask import request
import json
from termcolor import colored
import time
import os

class Market(Read_sheet):

    def read_excel_sheet(self):
        self.value = Read_sheet.reed_google(self)
        return self.value

    def rrsp_stat(self):
        print("")
        print("***R***")
        print("")
        result = self.value
        for i in range(25, 30):
            sym = result[i][0]
            sym = sym.upper()
            price = result[i][7].replace(",", "")
            price = float(price)
            if price > 0:
                print(colored("{} is up now by {}".format(sym, price), 'green'))
            else:
                print(colored("{} {}".format(sym, price), 'red'))
        return result

    def tfsa_stat(self):
        gains = []
        print("")
        print("***T***")
        print("")
        result = self.value
        for i in range(18, 22):
            sym = result[i][9]
            sym = sym.upper()
            price = result[i][16].replace(",", "")
            price = float(price)
            if price > 0:
                print(colored("{} is up now by {}".format(sym, price), 'green'))
            else:
                print(colored("{}  {}".format(sym, price), 'red'))

    def get_result(self):
        while True:
            Market.read_excel_sheet(self)
            Market.rrsp_stat(self)
            Market.tfsa_stat(self)
            time.sleep(10)
            bashCommand = "clear"
            os.system(bashCommand)

def main():
    call = Market()
    call.read_excel_sheet()
    call.get_result()
    
if __name__ == '__main__':
    main()
