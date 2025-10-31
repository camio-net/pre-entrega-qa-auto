from selenium.webdriver.common.by import By
from selenium import webdriver 
import pytest

from utils.datos import leer_csv_login
from pages.loginPage import LoginPage

leer_csv_login("datos/datos_usuarios_invalidos.csv")
def test_login_validation(login_page,usuario,password,debe_funcionar):
    driver = login_page
    print(debe_funcionar)
    if debe_funcionar == 'True':
        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"
    elif debe_funcionar == 'False':
        mensaje_error = LoginPage(driver).obtener_error()
        assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"

