from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.login_page import login_page as login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    login(driver).abrir_pagina().login("standard_user", "secret_sauce")
    return driver