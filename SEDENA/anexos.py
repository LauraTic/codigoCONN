import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import StaleElementReferenceException

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


df = pd.read_excel('/Users/datos-lc/Documents/Colecciones ongoing/SEDENA/2022/2022.xlsx')

url_procesar = df['enlace']

for i in range(len(url_procesar)):
    print(url_procesar[i])

    driver.get(url_procesar[i])
    time.sleep(10)

    expediente_pagina = driver.find_element(By.XPATH, "//div[@class='form_container'][1]/ul/li/div[@class='form_answer']").text.strip()
    print(expediente_pagina)

    anexos = driver.find_elements(By.XPATH, "//h3[@class='paragraph']")
    for anexo in anexos:
        texto = anexo.text
        if "Anexo" in texto:
            print("Tiene anexos")
            tablas = driver.find_elements(By.XPATH, "//tbody")
            tabla_anexo = tablas[-1]
            enlaces = tabla_anexo.find_elements(By.TAG_NAME, "a")
            
            print("Cantidad de enlaces de anexos")
            print(len(enlaces))

            for enlace in enlaces:
                time.sleep(10)
                print("Enlace actual: ")
                print(enlace)
                enlace.click()
                time.sleep(18)
                ruta_descargas = '/Users/datos-lc/Downloads/'
                ruta_contrato = '/Users/datos-lc/Documents/Colecciones ongoing/SEDENA/Anexos/'
                archivos_descargados = os.listdir(ruta_descargas)
                cantidad = len(archivos_descargados)
                print("La cantidad de archivos en la carpeta descargas es: ")
                print(cantidad)

                try:
                    if cantidad > 0:
                        for archivo in archivos_descargados:
                            time.sleep(10)
                            ruta_vieja = os.path.join(ruta_descargas, archivo)
                            nombre_archivo = expediente_pagina + " - " + archivo
                            ruta_nueva = os.path.join(ruta_contrato, nombre_archivo)
                            time.sleep(10)
                            try:
                                os.rename(ruta_vieja, ruta_nueva)
                                print("Archivo guardado")
                                print(archivo)
                                time.sleep(5)
                            except FileNotFoundError:
                                print(f"Archivo no encontrado: {ruta_vieja}")
                    else:
                        print("No se encontraron archivos en la carpeta de descargas.")
                        print(url_procesar[i])
                except StaleElementReferenceException:
                    print("Error con los PDFs")
                    continue
        else:
            print("No tiene anexo")
            

            
            





























