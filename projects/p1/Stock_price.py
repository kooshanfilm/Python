import request


class Stock_price():

    def check_price (self,stock_symbol):
        send_request = requests.get('https://api.iextrading.com/1.0/stock/{}/price'.format(stock_symbol))
        requests_json = send_request.json()
        return requests_json


    def check_change(self,stock_symbol):
        send_request = requests.get('https://api.iextrading.com/1.0/stock/{}/chart/1d'.format(stock_symbol))





