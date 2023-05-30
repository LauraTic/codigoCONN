import os
import pandas as pd
import re
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Función para hacer scroll hacia abajo de forma incremental
def scroll_incremental(driver):
    scrollable_element = driver.find_element(By.XPATH, "//body")
    for _ in range(5):  # Realizar 5 desplazamientos hacia abajo
        ActionChains(driver).move_to_element(scrollable_element).click().send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)



pagina_web = 'https://directoriosancionados.apps.funcionpublica.gob.mx/#'
driver = webdriver.Chrome()
driver.get(pagina_web)


# Seleccionar la opción "Todos" en el selector de la página
select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='cfiltro']")))
select_element.click()
option_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='cfiltro']/option[4]")))
option_element.click()

scrolled = 0
scroll_actual = 200
scroll_incremento = 500

while scrolled < 10:
    driver.execute_script(f"window.scrollTo(0, {scroll_actual});")
    time.sleep(0.5)
    scroll_actual += scroll_incremento
    scrolled += 1



# Lista de nombres y clicks en detalles
time.sleep(2)
#titulos = driver.find_elements(By.XPATH, "//table[@class='z-depth-1 table']/tbody/tr/th")
elementos = driver.find_elements(By.XPATH, "//tr[@class='ng-star-inserted']/td[4]/a")

diccionario = {}
nombres_columnas = ["Infractor", "Expediente", "Notificación_resolución", "Publicación_DOF", "Monto_multa", "Periodo_inhabilidad", "Inicia", "Termina", "Observaciones", "Objeto_social_infractor", "Causa", "OIC_Responsable", "Responsable_Información", "Cargo", "Teléfono", "Correo"]
contador = 0
for elemento in elementos:
    try:
       
        time.sleep(3)
        elemento.click()

        time.sleep(3)
        #nombres = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/strong")
        contenidos = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/p")
        time.sleep(5)
        print("-----------------------------------------------------------------")
        
        if len(contenidos) == len(nombres_columnas):
            for i in range(len(nombres_columnas)):
                columna = nombres_columnas[i]
                contenido = contenidos[i].text
                if columna in diccionario:
                    diccionario[columna].append(contenido)
                else:
                    diccionario[columna] = [contenido]
        else:
            nombre = contenidos[0].text
            print("La lista de contenidos no tiene la misma longitud que la lista de nombres de columna", nombre)


        print(len(diccionario))

        close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='p-ripple p-element ng-tns-c59-2 p-dialog-header-icon p-dialog-header-close p-link ng-star-inserted']")))
        close_button.click()
        time.sleep(5)

    except Exception as e:
       # nombre = contenidos[0].text
        print(f"Error al procesar el elemento: {e}")
        continue
        time.sleep(5)


print(diccionario)

time.sleep(3)
driver.quit()
df = pd.DataFrame(diccionario)
df.to_csv("/Users/connectasimac/Documents/DATOS/CODIGO/codigoCONN/diccionario.csv", index=True)

print("TERMINA CÓDIGO")

