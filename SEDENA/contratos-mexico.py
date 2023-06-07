### código para descargar los pdfs de los enlaces de cada contrato en la página de contratación de México. Descarga todos los archivos en pdf y crea uan carpeta con el nombre del expediente apra guardarlos################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from highlight_sel_element import highlight
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import re
import time
#import PyPDF2
import collections
import requests
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

############ codigo para descargar elementos faltantes en anterior iteración ################
def cambiar_nombre(filename):
    invalid_chars = [":", "/", "\\", "?", "*", "|", "<", ">", '"']
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    return filename 


df = pd.read_excel('/Users/datos-lc/Documents/Colecciones ongoing/SEDENA/faltantes.xlsx')
carpeta_descargas = os.path.expanduser('/Users/datos-lc/Downloads/')

procesados = []
no_descargados = []  # Lista para almacenar los posibles errores
descargados = []  # Lista para almacenar los contratos descargados

### for que usa dos parámetros del dataframe. Para cada una de esas columnas hace las búsquedas y descargas.
for columna1, columna2 in zip(df['Código del expediente'], df['Dirección del anuncio']):
   
    # Número del expediente que aparece en la columna del excel, para comprobar después que sí sea ese el contrato descargado
    expediente_excel = str(columna1)

    # Navegar en este enlace
    driver = webdriver.Chrome(columna2)
    driver.get(columna2)
    
    # Obtener el titulo con información del expediente y nombre del contrato que aparece en la página, sirve para nombrar la carpeta con los PDFs
    titulo = driver.find_element(By.XPATH, "//div[@class='subtitle_01 maintitle']")
    nombre_carpeta_contrato = titulo.text.strip()

    # Ruta completa de la carpeta para los archivos del contrato
    ruta_contrato = os.path.join(f'/Users/datos-lc/Documents/Colecciones ongoing/SEDENA/2022/', nombre_carpeta_contrato)
    
#Si la carpeta con el nombre del contrato existe, ya tiene contenido

    if os.path.exists(ruta_contrato):
        
        print(f"la carpeta{nombre_carpeta_contrato} ya tiene contenido")
        print(" ------------------------------------------------------")
        driver.quit()
#Si no existe no ha sido descargada y procede a crear la carpeta y buscar los pdf para descargarlos.       
    else:
        #Crea la carpeta
        os.makedirs(ruta_contrato)
        print(f"la carpeta{nombre_carpeta_contrato} NO EXISTEEEEEEEEEEE") 
        print(" ------------------------------------------------------")
       # Leer el número del expediente que aparece en la página web que estamos navegando
        aux = driver.find_element(By.XPATH, "//div[@class='form_container'][1]/ul/li/div[@class='form_answer']")
        expediente_pagina = aux.text.strip()

        #Crear la lista con los elementos descargables
        pdf = driver.find_elements(By.XPATH, "//a[@class='attachTaglink']")
        cantidad_pdf = len(pdf)
        print(cantidad_pdf)

#Cada archivo en pdf se le da click para descargar, si no cargó la página guarda la información que puede y continúa
        for archivo in pdf:
            try:
                archivo.click()
                time.sleep(11)
            except StaleElementReferenceException:
                print("Elemento obsoleto. Se omitirá y continuará con el siguiente.")
                print(nombre_carpeta_contrato)
                print(columna2)
                no_descargados.append([nombre_carpeta_contrato, cantidad_pdf, expediente_excel, expediente_pagina, columna2])
                continue
            
#Hace una lista de los archivos descargados DEBE ESTAR VACIA LA CARPETA DE DESCARGAS ANTES DE INICIAR EL CODIGO
        ruta = '/Users/datos-lc/Downloads/'
        ruta_contrato_edit = ruta_contrato + "/"
        files = os.listdir('/Users/datos-lc/Downloads/')
        try:

            if len(files)> 0:

                for descargado in files:
                    descargado_editado=cambiar_nombre(descargado)
                    ruta_vieja = os.path.join(ruta, descargado_editado)
                    ruta_nueva = os.path.join(ruta_contrato_edit, descargado_editado)
                    time.sleep(4) 
                    os.rename(ruta_vieja, ruta_nueva)
                    descargados.append([nombre_carpeta_contrato, cantidad_pdf, expediente_excel, expediente_pagina, descargado, columna2])
                    time.sleep(2)
            else:
                print("No se encontraron archivos en la carpeta de descargas.")
                no_descargados.append([nombre_carpeta_contrato, cantidad_pdf, expediente_excel, expediente_pagina])

            driver.quit()
        
        except StaleElementReferenceException:
            print("Error con los pdfs")
                
            continue



df_no_descargados = pd.DataFrame(no_descargados, columns=["Titulo_contrato", "Nro_pdfs_en_contrato", "Expediente_excel", "Expediente_pagina"])
df_descargados = pd.DataFrame(descargados, columns=["Titulo_contrato", "Nro_pdfs_en_contrato", "Expediente_excel", "Expediente_pagina", "Nombre_archivo_descargado", "URL" ])
df_descargados.to_csv('/Users/datos-lc/Documents/Colecciones ongoing/SEDENA/2022/descargados.csv', index=False)
df_no_descargados.to_csv('/Users/datos-lc/Documents/Colecciones ongoing/SEDENA/2022/no-descargados.csv', index=False)
