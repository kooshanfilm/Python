from pages.login import *
from pages.orders import *
from pages.patients import *
from pages.hcps import *


import unittest

class LoginTestCase(unittest.TestCase):

    # def test_login(self):
    #     call = LoginPage()
    #     call.open_the_page('ide')
    #     call.sign_in_without_password()
    #     call.sign_in()

    def test_login_with_microsoft(self):
        call = LoginPage()
        call.open_the_page('ide')
        call.sign_in_with_microsoft()
        # call.sign_in()

    # def test_orders_page(self):
    #     call = OrdersPage()
    #     call.order_page()
    #

    def test_patioents_page(self):
        call = PatientsPage()
        call.patients_page()
        call.create_order()
        # call.create_mx()

    # def test_healthcare_page(self):
    #       call = HcpsPage()
    #       call.hcps_page()

    def test_tear_down(self):
        call = OptBrowser()
        call.quit()

if __name__ == '__main__':
    unittest.main()



