from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.loginPage import login_page as login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver,usuario,password):
    login(driver).abrir_pagina().login(usuario,password)
    return driver