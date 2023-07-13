import os
import pandas as pd
import re
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


# Función para hacer scroll hacia abajo de forma incremental
def scroll_incremental(driver):
    scrollable_element = driver.find_element(By.XPATH, "//body")
    for _ in range(5):  # Realizar 5 desplazamientos hacia abajo
        ActionChains(driver).move_to_element(scrollable_element).click().send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)


import os
import pandas as pd
import re
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request


pagina_web = 'https://directoriosancionados.apps.funcionpublica.gob.mx/#'
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get(pagina_web)



# Seleccionar la opción "Todos" en el selector de la página
select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='cfiltro']")))
select_element.click()
option_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='cfiltro']/option[4]")))
option_element.click()

# Lista de nombres y clicks en detalles
time.sleep(2)
titulos = driver.find_elements(By.XPATH, "//table[@class='z-depth-1 table']/tbody/tr/th")
elementos = driver.find_elements(By.XPATH, "//tr[@class='ng-star-inserted']/td[4]/a")

diccionario = {}
contador = 0
for elemento, titulo in zip(elementos, titulos):
    try:
        titulo_texto = titulo.text
        print("##############################")
        print(titulo_texto)
        time.sleep(3)
        elemento.click()

        time.sleep(3)
        nombres = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/strong")
        contenidos = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/p")
        time.sleep(5)
        print("-----------------------------------------------------------------")
        tuplas = []

        for i in range(len(nombres)):
            nombre = nombres[i].text
            contenido = contenidos[i].text
            tupla = (nombre, contenido)
            tuplas.append(tupla)

        diccionario[titulo_texto] = tuplas
        print(len(diccionario))

        close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='p-ripple p-element ng-tns-c59-2 p-dialog-header-icon p-dialog-header-close p-link ng-star-inserted']")))
        close_button.click()
        time.sleep(5)
        contador += 1
    except Exception as e:
        print(f"Error al procesar el elemento: {e}")
        print(titulo_texto)
        continue
        time.sleep(5)

    if contador % 4 == 0:
            scroll_incremental(driver)

print(diccionario)

time.sleep(3)
driver.quit()

print("TERMINA CÓDIGO")

