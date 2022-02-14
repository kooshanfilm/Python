from splinter.browser import Browser
from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui

class OptBrowser(object):

    # driver = Browser('chrome', headless= False)
    driver = webdriver.Chrome()
    base_url_sit = 'https://cris-web-mvp-int.azurewebsites.net/'
    base_url_ide = 'https://cris-web-mvp-dev.azurewebsites.net/#/home'

    def find_element(self, *locator):
        return self.browser(*locator)

    def visit(self,enviroment):

        if enviroment =='sit':
            self.driver.get(self.base_url_sit)
        elif enviroment =='ide':
            self.driver.get(self.base_url_ide)

    def quit(self):
        self.driver.close()

    def wait(self,how_long):
        time.sleep(how_long)

    # def find_element_by_xpath(self):


