from tests.acceptance.locators.home_page import HomePageLocators


class HomePage:
    def __init__(self,driver):
        self.driver = driver


    def url(self):
        return 'http://127.0.0.1:5000/'

    def title(self):
        return self.driver.find_element(*HomePageLocators.title)

    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.title)