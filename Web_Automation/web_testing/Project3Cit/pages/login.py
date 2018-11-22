from pages.opt_browser import OptBrowser
from splinter.browser import Browser
from locators import *



class LoginPage(OptBrowser):

    def open_the_page(self):
        OptBrowser.driver.visit(OptBrowser.base_url)

    def accept_terms_of_service(self):
        OptBrowser.driver.click_link_by_id(LoginPagelocators.agree_terms_and_conditions)
        OptBrowser.driver.find_by_name(LoginPagelocators.continue_button).click()

    def choose_identification_Type(self):
        Identification_list = OptBrowser.driver.find_by_id(LoginPagelocators.choose_identification_type)
        Identification_list.find_by_xpath(LoginPagelocators.choose_client_id_number).click()

    def application_info(self,app_number,last_name):
        OptBrowser.driver.find_by_xpath(LoginPagelocators.application_number).fill(app_number)
        OptBrowser.driver.find_by_xpath(LoginPagelocators.application_last_name).fill(last_name)
        OptBrowser.driver.find_by_id(LoginPagelocators.choose_date_of_birth)
        OptBrowser.driver.find_by_xpath(LoginPagelocators.choose_date_of_birth_fild).click()
        OptBrowser.driver.execute_script(LoginPagelocators.insert_date_of_birth)
        OptBrowser.driver.find_by_xpath(LoginPagelocators.choose_place_of_birth).click()

    def application_final_status(self):
        OptBrowser.driver.find_by_xpath(LoginPagelocators.current_status).text





