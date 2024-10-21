from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#driver.get("https://www.turnitin.com/login_page.asp?lang=en_us")#
driver.get("https://www.turnitin.com/login_page.asp?lang=en_us")
correo = driver.find_element(By.ID, "email")
correo.send_keys("davidandrestinjaca@gmail.com")
time.sleep(2)

clave = driver.find_element(By.NAME, "user_password")
clave.send_keys("52Andres52@tinjaca")
time.sleep(2)

boton = driver.find_element(By.CLASS_NAME, "submit")
boton.click()
time.sleep(2)

driver.quit()