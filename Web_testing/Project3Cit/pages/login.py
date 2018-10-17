from pages.opt_browser import OptBrowser
from splinter.browser import Browser
from locators import *



class LoginPage(OptBrowser):

    def open_the_page(self):
        OptBrowser.driver.visit(OptBrowser.base_url)


    def accept_terms_of_service(self):
        OptBrowser.driver.click_link_by_id(LoginPagelocators.agree_terms_and_conditions)
        OptBrowser.driver.click_link_by_id(LoginPagelocators.continue_button)
        OptBrowser.driver.click_link_by_id(LoginPagelocators.choose_identification_type)




    server_list = browser.find_by_id('idTypeLabel')
    server_list.find_by_xpath("//*[@id='idTypeLabel']/option[2]").click()
    browser.find_by_xpath("//*[@id='idNumberLabel']").fill('54667184')
    browser.find_by_xpath("//*[@id='surnameLabel']").fill('Rostamzadeh Torghabeh')

    # def choose_right_application(self):
    #     OptBrowser.driver.