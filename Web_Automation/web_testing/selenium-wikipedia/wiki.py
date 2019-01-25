from selenium import webdriver
from locators import wikipediaHomepage, wikipediaArticle
from selenium.webdriver.common.keys import Keys
import time


driver =  webdriver.Chrome()
driver.get("https://en.wikipedia.org")
random_link = driver.find_element(*wikipediaHomepage.Random_Link)
random_link.click()
first_heading = driver.find_element(*wikipediaArticle.Frist_heading)
print (first_heading.text)
page_Info = driver.find_element(*wikipediaArticle.page_Info)
page_Info.click()

time.sleep(5)
search = driver.find_element(*wikipediaArticle.seach_Box)
search.send_keys('Canada' +Keys.RETURN)
time.sleep(5)

logo = driver.find_element(*wikipediaArticle.logo)
logo.click()
