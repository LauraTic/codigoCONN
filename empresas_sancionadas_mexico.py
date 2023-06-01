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

pagina_web = 'https://directoriosancionados.apps.funcionpublica.gob.mx/#'
driver =webdriver.Chrome()
driver.get(pagina_web)


# Seleccionar la opción "Todos" en el selector de la página
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='cfiltro']"))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='cfiltro']/option[4]"))).click()


"""# Realizar la acción de "Enter" en el elemento de entrada de texto
actions = ActionChains(driver)
actions.move_to_element(input_element)
actions.send_keys(Keys.ENTER)
"""


# Desplazar la página gradualmente y capturar elementos
scroll_incremento = 200  # Incremento de desplazamiento en píxeles
scroll_actual = 200  # Posición de desplazamiento actual
scrolled = 0 
elementos_capturados = []
elementos_faltantes = []

while scrolled < 10:
    driver.execute_script(f"window.scrollTo(0, {scroll_actual});")
    time.sleep(0.5)
    scroll_actual += scroll_incremento
    scrolled += 1

# Lista de nombres y clicks en detalles
time.sleep(2)
#titulos = driver.find_elements(By.XPATH, "//table[@class='z-depth-1 table']/tbody/tr/th")
detalles = driver.find_elements(By.XPATH, "//tr[@class='ng-star-inserted']/td[4]/a")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("SOY LA CANTIDAD DE DETALLES QUE HAY EN LA PRIMERA PAGINA")
print(detalles)
print(len(detalles))
contador =1
for i in range(len(detalles)):
    elemento = driver.execute_script("arguments[0].scrollIntoView();", detalles[i])
    time.sleep(3)
    detalles[i].click()
    print("SOY EL NÚMERO DEL DETALLE AL QUE ESTAMOS INGRESANDO")
    print(contador)
    nombres = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/strong")
    print("VOY A IMPRIMIR LA TABLA")
    print(nombres)
    print(len(nombres))
    """for i in nombres:
        i.text
        print(i)"""
       
    #contenidos = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/p")
   
   # print(len(contenidos))
    #print(contenidos)
    time.sleep(2) 
    close = driver.find_elements(By.XPATH, "//button[@class='p-ripple p-element ng-tns-c59-2 p-dialog-header-icon p-dialog-header-close p-link ng-star-inserted']")
    close.click()
    #close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='p-ripple p-element ng-tns-c59-2 p-dialog-header-icon p-dialog-header-close p-link ng-star-inserted']")))
    #close_button.click()
    time.sleep(2)  # Esperar 2 segundos después de cerrar la ventana emergente
    contador += 1

"""contador = 0
for i in range(len(detalles)):
    actions = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView();", detalles[i])
    uno = driver.find_element(By.XPATH, f"//tr[@class='ng-star-inserted']/td[4]/a[{i}]")
    detalles[i].click()
    time.sleep(3)
    close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='p-ripple p-element ng-tns-c59-2 p-dialog-header-icon p-dialog-header-close p-link ng-star-inserted']")))
    close_button.click()
    time.sleep(3)
"""

"""


diccionario = {}
nombres_columnas = ["Infractor", "Expediente", "Notificación_resolución", "Publicación_DOF", "Monto_multa", "Periodo_inhabilidad", "Inicia", "Termina", "Observaciones", "Objeto_social_infractor", "Causa", "OIC_Responsable", "Responsable_Información", "Cargo", "Teléfono", "Correo"]
contador = 0
for elemento in detalles:
    try:
        elemento.click()
        time.sleep(3)
        nombres = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/strong")
        contenidos = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/p")
        time.sleep(5)
        print("-----------------------------------------------------------------")
        
        contador = 0
        for i in range(len(nombres)):
            fila = nombres[i].text
            contenido = contenidos[i].text

            if fila in diccionario:
                diccionario[fila].append(contenido)
            else:
                diccionario[fila] = [contenido]

        print(len(diccionario))
        print(diccionario)
        df = pd.DataFrame(diccionario)
        df.to_csv(f"/Users/connectasimac/Documents/DATOS/CODIGO/codigoCONN/diccionario{contador}.csv", index=True)
        contador += 1
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


print("TERMINA CÓDIGO")

"""