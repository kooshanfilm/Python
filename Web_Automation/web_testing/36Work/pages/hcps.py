from lib2to3.pgen2 import driver
from opt_browser import OptBrowser
from splinter.browser import Browser
from locators import *

class HcpsPage(OptBrowser):

    def hcps_page(self):
        # click on the  L1 order page
        OptBrowser.driver.find_element_by_xpath(Homepagelocator.orders).click()




