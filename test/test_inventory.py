from selenium.webdriver.common.by import By
import pytest   
from pages.inventoryPage import inventory_page
from utils.datos import leer_csv_login

@pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/datos_usuarioValido.csv"))
def test_login_validation(login_page, usuario, password, debe_funcionar):
    try:
        driver = login_page
        inventory = inventory_page(driver)

        #Validacion del titulo de la pagina y la presencia de productos
        assert driver.title == "Swag Labs", "El título de la página no es correcto"
        
        #Validar que hay productos en el inventario
        productos = inventory.obtener_items_inventario()

        #Validar carrito esta vacio
        #assert inventory.obtener_cantidad_carrito() == 0, "El carrito no está vacío"
        #Validar agregar primer producto al carrito
        inventory.agregar_item_al_carrito()
        #Validar que el carrito tiene 1 producto
        assert inventory.obtener_cantidad_carrito() == 1, "El carrito no tiene producto"
        

    except Exception as e:
        print(f"Error en test_login_validation: {e}")
        raise
    finally:
        driver.quit()

