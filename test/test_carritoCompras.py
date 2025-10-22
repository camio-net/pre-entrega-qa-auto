from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_carrito_compras(logged_in_driver):
    try:
        driver = logged_in_driver

        # Agregar primer producto al carrito y validar
        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
        productos[0].find_element(By.TAG_NAME,"button").click()
        carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_link").text
        assert carrito == "1", "El producto no se agregó al carrito correctamente"
        print("Producto agregado al carrito correctamente.") 

        # Navegar al carrito de compras y validar 
        driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
        pagina = driver.current_url
        assert "/cart.html" in pagina, "No se navegó al carrito de compras"
        print("Navegación al carrito de compras exitosa.")

        #Remover el producto del carrito y validar
        productos_carrito = driver.find_elements(By.CLASS_NAME,"cart_item")
        productos_carrito[0].find_element(By.TAG_NAME,"button").click()
        assert carrito == "1", "El producto no se agregó al carrito correctamente"

    except Exception as e:
        print(f"Error en test_carrito_compras : {e}")
        raise

    finally:
        driver.quit()