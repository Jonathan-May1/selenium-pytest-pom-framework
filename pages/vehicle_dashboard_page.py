from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class VehicleDashboardPage(BasePage):
    LOGIN_BUTTON = (By.ID, "login-button")
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    DASHBOARD_HEADER = (By.CLASS_NAME, "title")      # Real "Products" header after login
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def get_wireless_status(self):
        return self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER)).text

    def get_vehicle_parts_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))
