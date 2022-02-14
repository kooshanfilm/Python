from pages.MainAmazonPage import *
import unittest

class LoginTestCase(unittest.TestCase):

    def test_open_amazon_website(self):
        call = MainPage()
        call.open_the_page()

    def test_tear_down(self):
        call = OptBrowser()
        call.quit()

if __name__ == '__main__':
    unittest.main()



