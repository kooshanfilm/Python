
from PageObjectSample.Pages.Login import Login
from PageObjectSample.Pages.MainPage import MainPage

from selenium import webdriver

PATH = "/Users/krostamzadeh/Downloads/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get('https://opensource-demo.orangehrmlive.com/')
driver.implicitly_wait(3)

login = Login(driver = driver)
main_page = MainPage(driver = driver)

login.enter_username('Admin')
login.enter_password('admin123')
login.click_on_login_button()
main_page.check_main_page()

driver.quit()






