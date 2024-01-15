#self.driver.find_element(By.LINK_TEXT, "India").click()
#self.driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
#self.driver.find_element(By.XPATH, "//input[@class = 'btn btn-success btn-lg']").click()
from selenium.webdriver.common.by import By


class confirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.LINK_TEXT , "India")

    def countryName(self):
        return self.driver.find_element(*confirmPage.country)