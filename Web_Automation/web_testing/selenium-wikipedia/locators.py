from selenium.webdriver.common.by import By


class wikipediaHomepage(object):
    Random_Link = (By.CSS_SELECTOR,'#n-randompage')

class wikipediaArticle(object):
    Frist_heading = (By.CSS_SELECTOR,'.firstHeading')
    page_Info = (By.LINK_TEXT,'Page information')
    seach_Box = (By.NAME,'search')
    logo = (By.XPATH,'//*[@id="p-logo"]/a')