import os
import pandas as pd
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request


pagina = 'https://www.facebook.com/BusquedaJal/photos'

ruta = '/Users/datos-lc/Documents/Colecciones ongoing/Cédulas-desaparecidos/'
driver = webdriver.Chrome()
driver.get(pagina)

elementos_capturados = []  # Lista para almacenar los detalles de cada eleme

elementos = driver.find_elements(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1lliihq x5yr21d x1n2onr6 xh8yej3"]')
cantidad_elementos = len(elementos)
print(cantidad_elementos)
contador = 0

for elemento in elementos:
    detalle_elemento = {}
    elemento.click()
    time.sleep(15)

    descripcion_elemento = driver.find_element(By.XPATH, '//div[@class="xyinxu5 x4uap5 x1g2khh7 xkhd6sd"]')
    texto_descripcion = descripcion_elemento.text

    # Capturar la imagen y guardarla
    imagen_elemento = driver.find_element(
        By.XPATH, '//img[@class="x1bwycvy x193iq5w x4fas0m x19kjcj4"]')
    url_imagen = imagen_elemento.get_attribute('src')
    nombre_imagen = f"Cédula_{contador}"
    #urllib.request.urlretrieve(url_imagen, nombre_imagen)
    urllib.request.urlretrieve(
        url_imagen, f'/Users/datos-lc/Documents/Colecciones ongoing/Cédulas-desaparecidos/{nombre_imagen}.jpeg')
    detalle_elemento['imagen'] = nombre_imagen
    detalle_elemento['descripcion'] = texto_descripcion
    detalle_elemento['url'] = url_imagen
    elementos_capturados.append(detalle_elemento)
    contador += 1

    # Cerrar la ventana emergente
    cerrar_elemento = driver.find_element(
        By.XPATH, '//div[@aria-label="Cerrar"]')
    cerrar_elemento.click()
    time.sleep(1)


print(elementos_capturados)

df = pd.DataFrame(elementos_capturados)
df.to_csv('/Users/datos-lc/Documents/Colecciones ongoing/Cédulas-desaparecidos/archivo.csv', index=False)
