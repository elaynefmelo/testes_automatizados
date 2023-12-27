from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Criar uma variavel para receber o tipo de navegador que se deseja usar
browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://www.saucedemo.com/v1/') 

#find element() para encontrar um elemento na tela, cada elemento foi colocado dentro de uma variavel

#username = browser.find_element(By.ID, "user-name")
#password = browser.find_element(By.ID, "password")

#send_keys ira preencher os campos localizados a cima
#username.send_keys("standard_user")
#password.send_keys("secret_sauce")

auth_fields = browser.find_elements(By.XPATH, "//*[@class='form_input']")
print(auth_fields) #mostra os elementos que estão na variavel
print(len(auth_fields)) #mostra quantos estão na varievel

#assert, usado para dizer o que você espera 
assert len(auth_fields) == 2, "O numero de elementos encontrados é diferente do esperado"

time.sleep(5)

browser.quit()

#find elements() para encontrar mais de um elemento na tela