from pages.login import LoginPage
from selenium import webdriver


import unittest

class LoginTestCase(unittest.TestCase):

    def testlogin(self):
        try:
            # loginpage is from MainAmazonPage.py
            call = LoginPage()
            call.open_the_page()
            call.accept_terms_of_service()
            call.choose_identification_Type()
            call.application_info('54667184', 'Rostamzadeh Torghabeh')
            call.application_final_status()

        except:
            call.quit()



if __name__ == '__main__':
    unittest.main()
