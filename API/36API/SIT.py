from cookies_SIT import *

class ResponseAutomation(SetupCookies):

    def MainPage(self):

        api = ['patient/ConsultCallbackReport','order/dailySales','order/pharmacy?userId=-1',
               'hcp?userId=-1','patient/business?userId=-1','mx/pharmacy?userId=-1',
                'product/cics/1/0?userId=-1','ls/list?userId=-1',
               ]

        for call in api:
            response = requests.get('https://cris-web-mvp-int.azurewebsites.net/api/{}'.format(call), headers=SetupCookies.headers, params=SetupCookies.params, cookies=SetupCookies.cookies)
            print (call,response)

def main():
    call = ResponseAutomation()
    call.MainPage()

if __name__ == '__main__':
    main()
