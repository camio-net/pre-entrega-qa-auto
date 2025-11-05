from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from utils.datos import leer_csv_login
from pages.loginPage import login_page 

class inventory_page:
        
    url = "https://www.saucedemo.com/inventory.html"
    @pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/datos_usuarioValido.csv"))
    def test_login_validation(login_page, usuario, password, debe_funcionar):
        driver = login_page

    def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)

    #validacion del login exitoso
    def titulo_inventario(self):
        titulo = self.title == "Swag Labs"
        return titulo

    #funcion para saber cantidad de productos en inventario

    def cantidad_productos(self):
        productos = self.find_elements(By.CLASS_NAME, "inventory_item")
        return len(productos)


