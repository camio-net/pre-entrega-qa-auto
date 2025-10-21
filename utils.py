from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    
    time.sleep(3)



