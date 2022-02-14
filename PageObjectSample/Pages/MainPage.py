class MainPage:
    def __init__(self,driver):
        self.driver = driver
        self.dashbord_label_id = "menu_dashboard_index"


    def check_main_page(self):
        self.driver.find_elements('id',self.dashbord_label_id)
