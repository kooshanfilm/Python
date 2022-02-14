from Web_Automation.web_testing.Amazon.opt_browser import OptBrowser
from splinter.browser import Browser
from Web_Automation.web_testing.Amazon.locators import *

class MainPage(OptBrowser):

    def open_the_page(self):

        OptBrowser.visit(self)
        OptBrowser.driver.maximize_window()
