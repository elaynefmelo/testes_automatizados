from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://www.saucedemo.com/v1/') 

#mapear elementos necessarios
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

#send_keys()
username.send_keys("standard_user")
password.send_keys("secret_sauce")

#click()
btn_login.click()

#text
products_title = browser.find_element(By.XPATH, "//*[@class='product_label']")
print(products_title.text)
assert products_title.text == "Products"

#get_attribute()
img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
print(img_backpack.get_attribute("class"))
assert img_backpack.get_attribute("class") == "inventory_item_img"