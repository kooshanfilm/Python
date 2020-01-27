from opt_browser import OptBrowser
from splinter.browser import Browser
from locators import *

class PatientsPage(OptBrowser):

    # def open_the_page(self):
    #     OptBrowser.driver.visit(OptBrowser.base_url)

    def patients_page(self):
        # click on paitients on the main page
        OptBrowser.driver.find_element_by_xpath(Homepagelocator.patients).click()
        OptBrowser.wait(self, 1)

        # click on the first patient
        OptBrowser.driver.find_element_by_xpath(L1patients.first_patient).click()

        # click on the patient btn
        OptBrowser.driver.find_element_by_xpath(L1patients.patient_details_btn).click()
        OptBrowser.wait(self, 1)

    def create_order(self):
        # click on the orders
        OptBrowser.driver.find_element_by_css_selector(L1patients.order_btn).click()
        OptBrowser.wait(self, 1)

        # click on new order button
        OptBrowser.driver.find_element_by_css_selector(L1patients.new_order).click()
        OptBrowser.wait(self, 1)

        # click on enter mx_btn
        OptBrowser.driver.find_element_by_xpath(L1patients.enter_mx_btn).click()
        OptBrowser.wait(self, 1)

        # daily Quantity
        OptBrowser.driver.find_element_by_css_selector(L1patients.daily_quantity).send_keys('3')

        # maximum THC
        OptBrowser.driver.find_element_by_css_selector(L1patients.maximum_thc).send_keys('1')

        # period of Use
        OptBrowser.driver.find_element_by_css_selector(L1patients.period_of_use).send_keys('2')

        # click on next button
        OptBrowser.wait(self, 1)
        OptBrowser.driver.find_element_by_xpath(L1patients.next_btn).click()


        # select a health care provider
        OptBrowser.wait(self, 1)
        OptBrowser.driver.find_element_by_xpath(L1patients.health_care_provider).click()
        OptBrowser.wait(self, 1)
        # health care provider button
        OptBrowser.driver.find_element_by_xpath(L1patients.health_care_provider_btn).click()
        OptBrowser.wait(self, 1)

        # Next page
        OptBrowser.driver.find_element_by_css_selector(L1patients.new_order_next_btn).click()
        OptBrowser.wait(self, 1)
        # click and choose a a common issues
        OptBrowser.driver.find_element_by_xpath(L1patients.common_issues).click()
        OptBrowser.wait(self, 2)

        OptBrowser.driver.find_element_by_css_selector(L1patients.create_mx_btn).click()


        OptBrowser.driver.find_element_by_css_selector(L1patients.close_new_order_btn).click()

        OptBrowser.wait(self, 1)