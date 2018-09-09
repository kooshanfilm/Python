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

         price =requests.get('https://api.iextrading.com/1.0/?symbols=MSFT')
         print(price)


def main():
    call = Jadi()
    # call.btc_price()
    call.stock()


if __name__ == '__main__': main()
