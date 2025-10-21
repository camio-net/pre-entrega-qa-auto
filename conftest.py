import test
from selenium import webdriver
from utils import login
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    login(driver, "standard_user", "secret_sauce")
    return driver