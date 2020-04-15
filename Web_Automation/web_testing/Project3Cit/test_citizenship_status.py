# from splinter.browser import Browser
import time
import datetime
import requests


class Check_status:

    def send_sms(self):
        url = "https://rest.nexmo.com/sms/json"
        querystring = {"api_key": "6f612444", "api_secret": "w3Zo2sMhibUjx4DA", "to": "16044429075",
                       "from": "15878012283", "text": "Decision Made******Decision Made****"}
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "b2af3a4b-64ce-2b2b-6e73-0431528e73f0"
        }
        response = requests.request("POST", url, headers=headers, params=querystring)
        print(response.text)

    def open_browser(self):
        url = "https://services3.cic.gc.ca/ecas/authenticate.do"
        browser = Browser('chrome', headless=False)
        browser.visit(url)
        browser.click_link_by_id('agree')
        browser.find_by_name('_target1').click()

        server_list = browser.find_by_id('idTypeLabel')
        server_list.find_by_xpath("//*[@id='idTypeLabel']/option[2]").click()
        browser.find_by_xpath("//*[@id='idNumberLabel']").fill('54667184')
        browser.find_by_xpath("//*[@id='surnameLabel']").fill('Rostamzadeh Torghabeh')

        server_list2 = browser.find_by_id('cobLabel')
        server_list2.find_by_xpath("//*[@id='cobLabel']/option[118]").click()
        browser.execute_script("dobDate.value = '1987-04-13'")
        browser.find_by_xpath("//*[@id='wb-main-in']/div[2]/form/div[22]/input[1]").click()
        element = browser.find_by_xpath("//*[@id='wb-main-in']/div[2]/form/table/tbody/tr/td[2]/a").text
        #print(element)
        if element == 'Decision Made':
            Check_status.send_sms(self)
        browser.find_by_xpath("//*[@id='wb-main-in']/div[2]/form/table/tbody/tr/td[2]/a").click()
        time.sleep(0.99999)
        browser.quit

    def num_days(self):
        now = datetime.datetime.now()
        last_year = 2018
        last_month = 3
        last_day = 6
        now_month = now.month
        now_day = now.day
        dmonth = now_month - last_month
        dday = now_day - last_day
        print(dmonth, dday)
        days = dmonth * 30 + dday + 1
        print(days, 'days')

def main():

    obj = Check_status()
    obj.open_browser()
    obj.num_days()


if __name__ == "__main__":
    main()
