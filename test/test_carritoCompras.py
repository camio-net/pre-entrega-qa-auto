from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.datos import leer_csv_login

from pages.inventoryPage import inventory_page  
from pages.cartPage import cart_page


def test_carrito_compras(login_page):
   
    try:
        driver = login_page

        

    except Exception as e:
        print(f"Error en test_carrito_compras : {e}")
        raise

    finally:
        driver.quit()