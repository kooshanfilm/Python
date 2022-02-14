from cookies_IDE import *

class ResponseAutomation(SetupCookies):

    def MainPage(self):

        url = "https://crisapi-mvp-dev.azurewebsites.net/api/Patient/UnattachDocument"
        response = requests.get('https://cris-web-mvp-dev.azurewebsites.net/api/patient/ConsultCallbackReport',
                                headers=SetupCookies.headers, params=SetupCookies.params, cookies=SetupCookies.cookies)
        print (response)

        data = {"documentId":1309}
        r = requests.post(url,data,headers=SetupCookies.headers, params=SetupCookies.params, cookies=SetupCookies.cookies)

        print (r)


def main():
    call = ResponseAutomation()
    call.MainPage()

if __name__ == '__main__':
    main()
