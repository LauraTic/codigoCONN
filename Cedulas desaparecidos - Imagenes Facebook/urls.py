import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import uuid
from joblib import Parallel, delayed
import pandas as pd
import hashlib
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse


# Leer el archivo Excel
df = pd.read_csv("/Users/datos-lc/Documents/Colecciones ongoing/Cedulas-aguas/lista_urls.csv")

# Obtener la columna de URLs
columna_urls = df["URL"]

# Convertir la columna de URLs a una lista
urls = columna_urls.tolist()
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#print(len(urls))

contador = 0
elementos_capturados = []
elementos_faltantes = []

"""def get_variable_name(url):
    print("Esta es la URL para sacar el nombre: ", url)
    parsed_url = urlparse(url)
    variable_name = parsed_url.path.split('?fbid')[-1]
    return variable_name
"""

def enter_url(url):
    global contador, elementos_capturados, elementos_faltantes
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver_local = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver_local.get(url)

    time.sleep(5)
    
    detalle_elemento = {}
    detalle_error = {}
    try:
        descripcion_elemento = driver_local.find_element(By.XPATH, '//div[@class="xyinxu5 x4uap5 x1g2khh7 xkhd6sd"]')
        texto_descripcion = descripcion_elemento.text
        texto_descripcion = texto_descripcion.replace('\n', ' ')
       
        imagen_elemento = driver_local.find_element(
            By.XPATH, '//img[@class="x85a59c x193iq5w x4fas0m x19kjcj4"]')
        
      
        url_imagen = imagen_elemento.get_attribute('src')
        #print("url_imagen", url_imagen)
        
        nombre_imagen = hashlib.sha256(bytes(url_imagen, 'utf-8')).hexdigest()
        #nombre_imagen = get_variable_name(url)
        print(nombre_imagen) 
        detalle_elemento['imagen'] = nombre_imagen
        detalle_elemento['descripcion'] = texto_descripcion
        detalle_elemento['url'] = url_imagen
        elementos_capturados.append(detalle_elemento)
        print(elementos_capturados)
        #print(detalle_elemento)
        
        #urllib.request.urlretrieve(url_imagen, nombre_imagen)
        urllib.request.urlretrieve(url_imagen, f'/Users/datos-lc/Documents/Colecciones ongoing/Aguas calientes/{nombre_imagen}.jpeg')
        
        
    except NoSuchElementException:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("                                                                 ")
        print("no lo pudimos encontrar", url)
        detalle_error['url'] = url
        elementos_faltantes.append(detalle_error)
        #print(elementos_faltantes)


    return detalle_elemento, elementos_capturados, elementos_faltantes
    contador += 1

"""for i in range(3):
    try:
        enter_url(urls[i])
    except NoSuchElementException:
        print("No se pudo, pana")"""

screenshots = Parallel(n_jobs=-1)(delayed(enter_url)(url) for url in urls)

df_capt = pd.DataFrame(screenshots)
df_falt = pd.DataFrame(elementos_faltantes)
df_capt.to_csv("/Users/datos-lc/Documents/Colecciones ongoing/Aguas calientes/capturados.csv", index=False)
df_falt.to_csv("/Users/datos-lc/Documents/Colecciones ongoing/Aguas calientes/faltantes.csv", index=False)
