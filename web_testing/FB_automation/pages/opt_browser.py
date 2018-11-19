from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options



class OptBrowser(object):

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')

    driver = webdriver.Chrome()
    base_url = 'http://www.facebook.com'

    def __init__(self):
        self.driver = OptBrowser.driver
        self.base_url =OptBrowser.base_url

    def quit(self):
        self.driver.close()

    def visit(self):
        self.driver.get(self.base_url)

