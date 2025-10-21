from selenium.webdriver.common.by import By
import pytest   

def test_inventory(logged_in_driver):
    try:
        driver = logged_in_driver
        
        assert driver.title == "Swag Labs", "El título de la página no es correcto"

        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encontraron productos en la página de inventario"
    
    except Exception as e:
        print(f"Error en test_inventory : {e}")    
        raise
    
    finally:
        driver.quit()   
        