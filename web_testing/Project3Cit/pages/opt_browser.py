from splinter.browser import Browser
from selenium import webdriver


class OptBrowser(object):

    driver = Browser('chrome', headless=False)
    base_url = 'https://services3.cic.gc.ca/ecas/authenticate.do'


    def find_element(self, *locator):
        return self.browser(*locator)

    def quit(self):
        self.driver.quit()

    def visit(self, location=''):
        url = self.base_url + location
        self.driver.get(url)