from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import os
import time

# Définir le chemin vers msedgedriver
driver_path = r"C:\Users\shinv\efrei\edgedriver\msedgedriver.exe"
service = Service(executable_path=driver_path)

options = webdriver.EdgeOptions()
options.add_argument("start-maximized")
options.add_argument(f"--user-data-dir={os.path.abspath('edge_temp_profile')}")

driver = webdriver.Edge(service=service, options=options)

# Charger le fichier local index.html
file_path = os.path.abspath("../index.html")
driver.get("file://" + file_path)

# ===============================
# Test 1 : Ajouter un utilisateur
# ===============================
name = "TestUser"
email = f"test{int(time.time())}@example.com"

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "form button").click()

time.sleep(2)  # attendre que l'utilisateur s'affiche

user_list_text = driver.find_element(By.ID, "userList").text
assert name in user_list_text and email in user_list_text
print("✅ Test ajout utilisateur : OK")

# ===============================
# Test 2 : Modifier l’utilisateur
# ===============================
new_name = "UserModifié"
edit_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), '✏️')]")
edit_buttons[-1].click()
time.sleep(1)

name_input = driver.find_element(By.ID, "name")
name_input.clear()
name_input.send_keys(new_name)
driver.find_element(By.CSS_SELECTOR, "form button").click()

time.sleep(2)

user_list_text = driver.find_element(By.ID, "userList").text
assert new_name in user_list_text
print("✅ Test modification utilisateur : OK")

# ===============================
# Test 3 : Supprimer l’utilisateur
# ===============================
delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), '❌')]")
delete_buttons[-1].click()
time.sleep(2)

user_list_text = driver.find_element(By.ID, "userList").text
assert new_name not in user_list_text
print("✅ Test suppression utilisateur : OK")

# ===============================
# Fin
# ===============================
driver.quit()
