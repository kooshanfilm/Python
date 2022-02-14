from opt_browser import OptBrowser
from splinter.browser import Browser
from locators import *



class LoginPage(OptBrowser):

    username = 'krostamzadeh@36eighttechnologies.com'
    password = 'e!*y&WF7J$8c'

    microsoft_username = 'krostamzadeh@36eighttechnologies.com'
    microsoft_password = 'Qu74CFl$j%46'


    def open_the_page(self,env):
        OptBrowser.visit(self,env)
        # maximize the windows
        OptBrowser.driver.maximize_window()

    def sign_in_without_password(self):
        OptBrowser.driver.find_element_by_id(LoginPagelocators.username_filed).send_keys(LoginPage.username)
        OptBrowser.driver.find_element_by_xpath(LoginPagelocators.Sing_in_button).click()

    def sign_in(self):
        OptBrowser.driver.find_element_by_id(LoginPagelocators.username_filed).clear()
        OptBrowser.driver.find_element_by_id(LoginPagelocators.username_filed).send_keys(LoginPage.username)
        OptBrowser.driver.find_element_by_id(LoginPagelocators.password_filed).send_keys(LoginPage.password)
        OptBrowser.driver.find_element_by_xpath(LoginPagelocators.Sing_in_button).click()

    def sign_in_with_microsoft(self):
        OptBrowser.driver.find_element_by_id(LoginMicrosoft.username_filed).send_keys(LoginPage.microsoft_username)
        OptBrowser.wait(self,1)
        OptBrowser.driver.find_element_by_id(LoginMicrosoft.next_btn).click()
        OptBrowser.driver.find_element_by_id(LoginMicrosoft.password_filed).send_keys(LoginPage.microsoft_password)
        OptBrowser.wait(self,1)
        OptBrowser.driver.find_element_by_id(LoginMicrosoft.next_btn).click()
        OptBrowser.wait(self,2)

        # un comment this if there is a YES/NO for keeping the user signed in
        # OptBrowser.driver.find_element_by_id(LoginMicrosoft.yes_btn).click()





