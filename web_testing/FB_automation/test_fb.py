from pages.login import LoginPage
from selenium import webdriver


import unittest

class LoginTestCase(unittest.TestCase):

    def testlogin(self):
            try:
                # loginpage is from login.py
                call = LoginPage()
                call.open_the_page()
                call.create_page()
                call.quit()

            except IOError:
                print (IOError)
                call.quit()


if __name__ == '__main__':
    unittest.main()
