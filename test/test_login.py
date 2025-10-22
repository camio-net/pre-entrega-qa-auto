from selenium.webdriver.common.by import By
from selenium import webdriver


def test_valid_login(logged_in_driver): 
    try:      
        driver = logged_in_driver
        pagina = driver.current_url
        assert  "/inventory.html" in pagina, "No se pudo iniciar sesión correctamente"
        print("Test de inicio de sesión exitoso.")
    except Exception as e:
        print(f"Test fallido debido a una excepción: {e}")    
        raise
    
    finally:
        driver.quit()
    


