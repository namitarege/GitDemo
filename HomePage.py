#self.driver.find_element(By.XPATH, "//a [contains(@href, 'shop')]").click()
from selenium.webdriver.common.by import By
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a [contains(@href, 'shop')]")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)
