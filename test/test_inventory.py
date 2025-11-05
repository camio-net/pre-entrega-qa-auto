from selenium.webdriver.common.by import By
import pytest   
from pages.inventoryPage import inventory_page







'''
def test_inventory(login_page):
    try:
        
        
        #Validacion del titulo de la pagina y la presencia de productos
        assert driver.title == "Swag Labs", "El título de la página no es correcto"
        print("Título de la página verificado correctamente.")
        
        #Validacion de la presencia de productos en la pagina
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encontraron productos en la página de inventario"
        print("Test de inventario exitoso.")

        #Leer el nombre y precio del primer producto
        nombreProducto = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        precioProducto = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text

        print(f"Primer producto encontrado: {nombreProducto} con precio {precioProducto}")


    except Exception as e:
        print(f"Error en test_inventory : {e}")    
        raise
    
    finally:
        driver.quit()   
        ''''''