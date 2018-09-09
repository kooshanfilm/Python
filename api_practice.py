import requests


class Jadi:

    def btc_price(self):
        response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
        j = response.json()
        print(j['data']['amount'])

    def send_sms(self):
        url = "https://rest.nexmo.com/sms/json"
        querystring = {"api_key": "6f612444", "api_secret": "w3Zo2sMhibUjx4DA", "to": "16044429075",
                       "from": "15878012283", "text": "%22Hello%20maximooz%20%22"}
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "b2af3a4b-64ce-2b2b-6e73-0431528e73f0"
        }
        response = requests.request("POST", url, headers=headers, params=querystring)
        print(response.text)

    def stock(self):

         send_request = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFT&apikey=1HTVZL0H0N34WT84')
         requests_json = send_request.json()
         current_price = float((requests_json['Global Quote']['05. price']))
         if current_price == 108.2100:
         	Jadi.send_sms(self)


def main():
    call = Jadi()
    # call.btc_price()
    call.stock()


if __name__ == '__main__': main()
