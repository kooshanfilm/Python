import unittest

from Locators import *

from Pages.Login import Login
from Pages.MainPage import MainPage
from selenium import webdriver


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None: #run only one before
        PATH = "/Users/krostamzadeh/Downloads/chromedriver"
        cls.driver = webdriver.Chrome(PATH)
        cls.driver.implicitly_wait(5)

    def test1(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        login = Login(driver = self.driver)
        main_page = MainPage(driver = self.driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_on_login_button()
        main_page.check_main_page()

    def test2(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username('Admin')
        login.enter_password('admin1234')
        login.click_on_login_button()
        main_page.check_main_page()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()








