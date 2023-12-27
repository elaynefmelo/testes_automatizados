from selenium import webdriver
import time

# Criar uma variavel para receber o tipo de navegador que se deseja usar
browser = webdriver.Chrome()

#maximize_window() maximizar a janela
browser.maximize_window()

#get() acessa uma pagina
browser.get('https://google.com')

#refresh()
browser.refresh()

browser.get('https://www.saucedemo.com/v1/')

time.sleep(2)

#back()
browser.back()
time.sleep(2)

#forward, clica na setinha para frente
browser.forward()
time.sleep(2)

#criar uma outra aba
#browser.switch_to.new_window("tab") 
#time.sleep(2)

#close
#browser.close()
#time.sleep(2)


#quit()
browser.switch_to.new_window("tab") 
browser.switch_to.new_window("tab") 
time.sleep(3)
browser.quit() #sempre deve ser
