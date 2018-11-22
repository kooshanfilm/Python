import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()



    def test_open_web(self):
        driver = self.driver
        driver.get("https://www.vfsvisaonline.com/Netherlands-Global-Online-Tracking_Zone1/TrackLanding.aspx")
          # seconds

        country = driver.find_element_by_xpath("// *[ @ id = 'plhMain_Table2'] / tbody / tr[1] / td[2] / div / div[1]")
        country.click()

        search_country = driver.find_element_by_xpath("//*[@id='plhMain_Table2']/tbody/tr[1]/td[2]/div/div[2]/div/input")
        search_country.send_keys("canada")

        language = driver.find_element_by_xpath("//*[@id='plhMain_Table2']/tbody/tr[4]/td[2]/div/div[1]")
        # language.click()
        #
        # search_language = driver.find_element_by_xpath("// *[ @ id = 'plhMain_Table2'] / tbody / tr[4] / td[2] / div / div[2] / div / input")
        language.send_keys("english")


        # submit_form = driver.find_element_by_id("plhMain_btnSubmit")
        # submit_form.click()
        #

    







    # def test_search_in_python_org(self):
    #
    #     driver.get("http://www.python.org")
    #     self.assertIn("Python", driver.title)
    #     elem = driver.find_element_by_name("q")
    #     elem.send_keys("pycon")
    #     elem.send_keys(Keys.RETURN)
    #     assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()