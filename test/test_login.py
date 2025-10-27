from selenium.webdriver.common.by import By
from selenium import webdriver


def test_valid_login(login_page): 
    try:      
        driver = login_page 
        pagina = driver.current_url
        assert  "/inventory.html" in pagina, "No se pudo iniciar sesión correctamente"
        print("Test de inicio de sesión exitoso.")
    except Exception as e:
        print(f"Test fallido debido a una excepción: {e}")    
        raise
    
    finally:
        driver.quit()
    


