from Locators import *

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = username_textbox_id
        self.password_textbox_id = password_textbox_id
        self.logibutton_id = logibutton_id

    def enter_username(self,username):
        self.driver.find_element('id', username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('id', password_textbox_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('id', logibutton_id).click()









