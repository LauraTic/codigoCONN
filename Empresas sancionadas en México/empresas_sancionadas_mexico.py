import os
import csv
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
from fpdf import FPDF

pagina_web = 'https://directoriosancionados.apps.funcionpublica.gob.mx/#'
driver = webdriver.Chrome()
driver.get(pagina_web)


# Seleccionar la opción "Todos" en el selector de la página
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='cfiltro']"))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='cfiltro']/option[4]"))).click()

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
titulos = driver.find_elements(By.XPATH, "//table[@class='z-depth-1 table']/tbody/tr/th")
expedientes = driver.find_elements(By.XPATH, "//table[@class='z-depth-1 table']/tbody/tr/td[@class='ng-star-inserted']")

time.sleep(2)
detalles = driver.find_elements(By.XPATH, "//tr[@class='ng-star-inserted']/td[4]/a")
contador =1
diccionario = {}

for i in range(len(detalles)):
    #Encontrar el elemento
    elemento = driver.execute_script("arguments[0].scrollIntoView();", detalles[i])
    time.sleep(3)
    detalles[i].click()
    print("Archivo #:", i)

    #CAPTURAR LOS DATOS EN LA TABLA
    time.sleep(4) 
    nombres = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/strong")
    time.sleep(4) 
    contenidos = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/p")
    
    #CONVERTIR LOS ELEMENTOS WEB EN TEXTO
    lista_nombres = [nombre.text for nombre in nombres]
    lista_contenidos = [contenido.text for contenido in contenidos]
    nombre = titulos[i].text
    aux = expedientes[i].text
    expediente = aux.replace("/", "-")

    # Crear el DataFrame
    df = pd.DataFrame({'Ficha técnica del infractor': lista_nombres, 'Datos': lista_contenidos})
    df = df.set_index('Ficha técnica del infractor')
    print(df)
    df.to_excel(f'/Users/connectasimac/Documents/DATOS/CODIGO/codigoCONN/{nombre}-{expediente}-.xslx', index=True)

        # Crear una clase personalizada basada en FPDF
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Ficha técnica del infractor', 0, 1, 'C')


    # Crear una instancia del objeto PDF
    pdf = PDF()
    pdf.add_page()

    # Configurar el ancho de las celdas y el tamaño de la fuente
    cell_width = 100
    font_size = 12

    # Leer el DataFrame y agregar los datos al PDF
    for index, row in df.iterrows():
        for column in df.columns:
            pdf.set_font('Arial', '', font_size)
            content = str(row[column])
            pdf.cell(cell_width, 10, content[:100], 1)  # Ajustar el contenido a la longitud de la celda
        pdf.ln()

    
    # Guardar el archivo PDF
    pdf.output(f'/Users/connectasimac/Documents/DATOS/CODIGO/codigoCONN/{nombre}-{expediente}.pdf')

    print("Archivo PDF guardado exitosamente.")


    close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='p-ripple p-element ng-tns-c59-2 p-dialog-header-icon p-dialog-header-close p-link ng-star-inserted']")))
    close_button.click()

    #
    #print(tabla_texto)
    # Guardar los datos en un archivo CSV
    
    



    """
    for i in range(len(nombres)):
            fila = nombres[i].text
            contenido = contenidos[i].text

            if fila in diccionario:
                diccionario[fila].append(contenido)
            else:
                diccionario[fila] = [contenido]

            print(diccionario)"""

    
       
    #contenidos = driver.find_elements(By.XPATH, "//table[@class='table table-striped table-fit table-bordered table-hover']/tbody/tr/td/p")
   
   # print(len(contenidos))
    #print(contenidos) 
    
    



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