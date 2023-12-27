from selenium import webdriver
import time

# Criar uma variavel para receber o tipo de navegador que se deseja usar
browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/v1/')

#title
print("O titulo da página é:",browser.title)

#current_url
print("A URL da página é:",browser.current_url)

#page_source
print("O código fonte da página é:",browser.page_source)
