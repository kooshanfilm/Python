from pages.login import LoginPage
from selenium import webdriver


import unittest

class LoginTestCase(unittest.TestCase):

    def testlogin(self):

        # loginpage is from login.py
        call = LoginPage()
        call.open_the_page()
        call.accept_terms_of_service()

        call.quit()





if __name__ == '__main__':
    unittest.main()
