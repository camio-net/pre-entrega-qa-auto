from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 
driver.implicitly_wait(5)

def new_func(driver):
    producto = driver.find_elements(By.CLASS_NAME,"inventory_item")
    producto [0].find_element(By.TAG_NAME,"button").click()
    carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_container").text
    assert carrito == "1"

try: 
    driver.get("https://www.saucedemo.com")
    
    #Validacion de credenciales
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    print ("Validacion de credecion exitosa, OK")


    #validadcion de pagina inventario inventory.html
    assert  '/inventory.html' in driver.current_url
    print ("Validacion de 'pagina invenory.html', ok")

    #interacciones
    
    new_func(driver)
    
    
    print("Ingreso a la pagina de navegacion, OK")
    time.sleep(2)
finally:
    driver.quit()
