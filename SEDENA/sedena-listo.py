import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import StaleElementReferenceException

options = FirefoxOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Firefox(options=options)

df = pd.read_excel('/Users/datos-lc/Documents/Colecciones ongoing/SEDENA/20199.xlsx')


url_procesar = df['enlace']


# Iterate over the rows of the DataFrame
for i in range(len(url_procesar)):
    # Navigate to the URL
    driver.get(url_procesar[i])
    time.sleep(2)
    
    # Find all the PDF links on the page
    pdf = driver.find_elements(By.XPATH, "//a[@class='attachTaglink']")
    expediente_pagina = driver.find_element(By.XPATH, "//div[@class='form_container'][1]/ul/li/div[@class='form_answer']").text.strip()
    cantidad_pdf = len(pdf)
    print("Los archivos leídos son:", cantidad_pdf)
    
    # Iterate over the PDF links and perform actions
    for archivo in pdf:
        try:
            time.sleep(4)
            archivo.click()
            time.sleep(10)
        except StaleElementReferenceException:
            print("Elemento obsoleto. Se omitirá y continuará con el siguiente.")
            print(expediente_pagina)
            print(url_procesar[i])
            continue
        
        ruta = '/Users/datos-lc/Downloads/'

        ruta_contrato = '/Users/datos-lc/Documents/Colecciones ongoing/SEDENA/2019-2/'
        files = os.listdir(ruta)
        cantidad = len(files)
                           
        try:
            if cantidad > 0:
                for descargado in files:
                    time.sleep(3)
                    ruta_vieja = os.path.join(ruta, descargado)
                    name = expediente_pagina + " - " + descargado
                    ruta_nueva = os.path.join(ruta_contrato, name)
                    try:
                        os.rename(ruta_vieja, ruta_nueva)
                        print("Archivo guardado")
                        print(url_procesar[i])
                        time.sleep(2)
                    except FileNotFoundError:
                        print(f"Archivo no encontrado: {ruta_vieja}")
            else:
                print("No se encontraron archivos en la carpeta de descargas.")
                print(url_procesar[i])
        except StaleElementReferenceException:
            print("Error con los pdfs")
            continue

driver.quit()
