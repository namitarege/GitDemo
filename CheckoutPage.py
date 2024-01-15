#self.driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")
#self.driver.find_element(By.CSS_SELECTOR, "a[class *='btn-primary']").click()
#self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class = 'card h-100']")
    buttonFooter = (By.CSS_SELECTOR, "a[class *='btn-primary']")
    successbutton = (By.XPATH, "//button[@class = 'btn btn-success']")

    def cardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getFooter(self):
        return self.driver.find_element(*CheckoutPage.buttonFooter)

    def succButton(self):
        return self.driver.find_element(*CheckoutPage.successbutton)