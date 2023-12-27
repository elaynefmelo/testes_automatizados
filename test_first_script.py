from selenium import webdriver
import time

# Criar uma variavel para receber o tipo de navegador que se deseja usar
browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/v1/')
time.sleep(10) 