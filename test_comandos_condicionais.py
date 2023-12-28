from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Criar uma variavel para receber o tipo de navegador que se deseja usar =
browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://demo.applitools.com/')

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")
enter

#is_displayed() para saber se o elemento se encontra na tela
print(username.is_displayed())
assert username.is_displayed()
#is_enablad() para saber se o elemento foi habilitado
print(username.is_enabled())
assert username.is_enabled() #eu espero que isso aqui nao seja falso
#is selected() saber se o checjbox ja está sendo selecionado
print(checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected() #eu espero que isso aqui seja falso

#clicando no checkbox
time.sleep(2)
checkbox_remember_me.click()
time.sleep(5)
print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected() 