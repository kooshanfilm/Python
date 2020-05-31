from config import *


class TestPyOrgBase(unittest.TestCase):
    """
    TBD
    """
    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('headless')
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


class TestHome(TestPyOrgBase):
    """
    TBD
    """
    def setUp(self):
        self.home = HomePage(TestHome.driver)


    def test_TC001_homepage(self):

        assert self.driver.current_url == 'https://www.amazon.ca/'
        self.home.click(HomePageLocators.MID_PAGE_SIGNIN)

    def test_TC001_dealsstore(self):
        self.home.click(DealsStorePageLocators.DEALSSTORE)

