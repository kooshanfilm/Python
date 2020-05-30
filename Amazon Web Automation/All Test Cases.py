from config import *


class TestPyOrgBase(unittest.TestCase):
    """
    TBD
    """
    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
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

    def test_TC001_py3_doc_button(self):
        assert self.driver.current_url == 'https://www.amazon.ca/'
