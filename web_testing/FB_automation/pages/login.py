from pages.opt_browser import OptBrowser
from splinter.browser import Browser
from locators import *



class LoginPage(OptBrowser):


    def open_the_page(self):
        OptBrowser.visit(self)

    def login(self):
        OptBrowser.driver.find_element_by_xpath(Loginpagelocators.login_button).click()

    def create_page(self):
        OptBrowser.driver.find_element_by_link_text(Loginpagelocators.create_page).click()







