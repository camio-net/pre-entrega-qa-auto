from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 
driver.implicitly_wait(5)

def test_login(usuario,password):
    
    try: 
    
        driver.get("https://www.saucedemo.com")   
        time.sleep(1)
        driver.find_element(By.ID,"user-name").send_keys(usuario)
        driver.find_element(By.ID,"password").send_keys(password)
        driver.find_element(By.ID,"login-button").click()
        print ("Validacion de credecion exitosa, OK")

        time.sleep(2)
        
        #validadcion de pagina inventario inventory.html
        assert  '/inventory.html' in driver.current_url, "No se direccion correctamente al inventario"
        print ("Validacion de 'pagina invenory.html', ok")

    except Exception as e:
        print(f"Error en test login {e}")
        raise 


#Validacion de productos en el inventario
def test_productos():

    producto = driver.find_elements(By.CLASS_NAME,"inventory_item")
    try:
        cantidad= len(producto)
        assert cantidad > 0
        print (f"La pagina tiene {cantidad} productos")
        print ("Validacion de productos en la pagina, ok")

    except Exception as e:
        print(f"Error en test procutos en el inventario {e}")
        raise 


#Validar agregar productos en el carrito de compras
def test_agregarProducto():

    try:
        test_login()
        time.sleep(2)
        producto = driver.find_elements(By.CLASS_NAME,"inventory_item")
        producto [0].find_element(By.TAG_NAME,"button").click()
        carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_container").text
        assert carrito == " "
    
    
    
    except Exception as e:
        print(f"Error al agregar producto: {e}")
        raise 