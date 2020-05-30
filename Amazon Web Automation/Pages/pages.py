from config import *


class BasePage:
    """
    Base Page class that hold common elements
    and functionalities to all pages in app
    """

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def assert_elem_text(self, by_locator, elem_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.text == elem_text


class HomePage(BasePage):
    """
    Home page of Amazon
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver.get("https://www.amazon.ca/")
