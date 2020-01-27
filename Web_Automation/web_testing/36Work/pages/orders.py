from lib2to3.pgen2 import driver
from opt_browser import OptBrowser
from splinter.browser import Browser
from locators import *

class OrdersPage(OptBrowser):

    def order_page(self):

        # click on the  L1 order page
        OptBrowser.driver.find_element_by_xpath(Homepagelocator.orders).click()
        OptBrowser.wait(self,1)

        # click on order details btn to select another iframe and choose the first order
        OptBrowser.driver.find_element_by_xpath(L1orderlocator.order_details_btn).click()
        OptBrowser.driver.find_element_by_xpath(L1orderlocator.first_order).click()

        # clicking on order details button
        OptBrowser.driver.find_element_by_xpath(L1orderlocator.order_details_btn).click()
        OptBrowser.driver.find_element_by_xpath(L1orderlocator.close_btn).click()
        OptBrowser.wait(self, 1)





















