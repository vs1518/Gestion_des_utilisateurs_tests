from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import os

# Chemin vers msedgedriver
driver_path = r"C:\Users\shinv\efrei\edgedriver\msedgedriver.exe"
service = Service(executable_path=driver_path)

options = webdriver.EdgeOptions()
options.add_argument("start-maximized")
options.add_argument(f"--user-data-dir={os.path.abspath('edge_temp_profile')}")


driver = webdriver.Edge(service=service, options=options)

# Ouvrir le fichier index.html
html_path = os.path.abspath("../index.html")  # ← corrige le chemin si nécessaire
driver.get("file://" + html_path)

# Ajouter un utilisateur
driver.find_element(By.ID, "name").send_keys("TestEdge")
driver.find_element(By.ID, "email").send_keys(f"test{int(time.time())}@mail.com")
driver.find_element(By.CSS_SELECTOR, "form button").click()
time.sleep(2)

# Modifier
edit_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), '✏️')]")
if edit_buttons:
    edit_buttons[-1].click()
    time.sleep(1)
    name_input = driver.find_element(By.ID, "name")
    name_input.clear()
    name_input.send_keys("ModifiéEdge")
    driver.find_element(By.CSS_SELECTOR, "form button").click()
    time.sleep(2)

# Supprimer
delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), '❌')]")
if delete_buttons:
    delete_buttons[-1].click()
    time.sleep(2)

driver.quit()
