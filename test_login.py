from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Validacion de credenciales
def test_login():
    driver = webdriver.Chrome() 
    driver.implicitly_wait(5)

    try: 
    
        driver.get("https://www.saucedemo.com")   
        time.sleep(1)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
        print ("Validacion de credecion exitosa, OK")

        time.sleep(2)
        
        #validadcion de pagina inventario inventory.html
        assert  '/inventory.html' in driver.current_url, "No se direccion correctamente al inventario"
        print ("Validacion de 'pagina invenory.html', ok")

    except Exception as e:
        print(f"Error en test login {e}")
        raise 

    finally:
        driver.quit()

    


    
    

    #interacciones
    '''
    producto = driver.find_elements(By.CLASS_NAME,"inventory_item")
    producto [0].find_element(By.TAG_NAME,"button").click()
    carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_container").text
    assert carrito == "1"
    

    #Validacion Pagina producto
    producto = driver.find_elements(By.CLASS_NAME,"inventory_item")
    nombre_producto = producto[0].find_element(By.CLASS_NAME,"inventory_item_name").text
    producto[0].find_element(By.CLASS_NAME,"inventory_item_name").click()
   
    tituloPaginaProducto = driver.find_element(By.CSS_SELECTOR, ".inventory_details_name.large_size").text
    assert nombre_producto == tituloPaginaProducto
    print("Validacion pagina producto, OK")


    
    print("Ingreso a la pagina de navegacion,Todo OK")
    time.sleep(2)
finally:
    driver.quit()
'''
