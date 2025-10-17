from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from formulasAux import *
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 
driver.implicitly_wait(5)

test_login("standard_user","secret_sauce")
test_productos()
test_agregarProducto()

