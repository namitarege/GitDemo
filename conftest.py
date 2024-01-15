import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        service_obj = Service()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=service_obj)
# here we can put elif and give other browser names like firefox and IE
# and then provide the particular browser name from terminal
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()
