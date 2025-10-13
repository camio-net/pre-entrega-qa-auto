from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 
driver.implicitly_wait(5)

try: 
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    

    print(driver.title)
    assert driver.title == "Swag Labs"

    time.sleep(5)
finally:
    driver.quit()