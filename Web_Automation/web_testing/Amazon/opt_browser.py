from splinter.browser import Browser
from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui

class OptBrowser(object):

    # driver = Browser('chrome', headless= False)
    driver = webdriver.Chrome()
    base_url = "https://www.amazon.ca/"

    # def find_element(self, *locator):
    #     return self.browser(*locator)

    def visit(self):
        self.driver.get(self.base_url)

    def quit(self):
        self.driver.close()

    def wait(self,how_long):
        time.sleep(how_long)

    # def find_element_by_xpath(self):


