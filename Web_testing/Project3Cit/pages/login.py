from pages.opt_browser import OptBrowser
from splinter.browser import Browser
from locators import *



class LoginPage(OptBrowser):

    def open_the_page(self):
        OptBrowser.driver.visit(OptBrowser.base_url)


    def accept_terms_of_service(self):
        OptBrowser.driver.click_link_by_id(LoginPagelocators.agree_terms_and_conditions)


    # def choose_right_application(self):
    #     OptBrowser.driver.