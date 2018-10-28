from quickstart import *
from flask import Flask, jsonify, Response
from flask import request
import json



class Market(Read_sheet):

    app = Flask(__name__)

    def read_excel_sheet(self):
        self.value = Read_sheet.reed_google(self)
        return self.value

    def rrsp_stat(self):
        print("")
        print("***RRSP***")
        print("")
        result = self.value
        for i in range(25,30):
            sym = result[i][0]
            price = result[i][7]
            print(sym.upper() +": "+ price)



    def tfsa_stat(self):
        print("")
        print("***TFSA***")
        print("")
        result = self.value
        for i in range(18,22):
            sym = result[i][9]
            price = result[i][16]
            print(sym.upper() + ": " + price)

    app.run(port=5000)

def main():
    call = Market()
    call.read_excel_sheet()
    call.rrsp_stat()
    call.tfsa_stat()


if __name__ == '__main__':
    main()
