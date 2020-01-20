from pages.login import LoginPage
from pages.login import OptBrowser
from selenium import webdriver

import unittest


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.username = "test"
        self.pasword = "test"
        self.call = LoginPage()

    def testlogin(self):
        # loginpage is from MainAmazonPage.py
        self.call.open_the_page()

    def testauth(self):
        self.call.open_the_page()
        self.call.auth(self.username,self.pasword)

    def testcheck_languages(self):
        self.call.check_language()

    # close the browser after the test
    def testtear_down(self):
        call = OptBrowser()
        call.quit()



if __name__ == '__main__':
    unittest.main()
