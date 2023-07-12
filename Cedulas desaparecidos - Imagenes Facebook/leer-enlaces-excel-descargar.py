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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Leer el archivo Excel
df = pd.read_csv("/Users/datos-lc/Documents/Colecciones ongoing/jalisco/url-jalisco.csv")

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

contador = 0

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def enter_url(url):
    global contador, elementos_capturados, elementos_faltantes, driver

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
   

    
    driver.get(url)

    time.sleep(5)
    

    try:
        texto_descripcion = driver.find_element(By.XPATH, '//div[@class="xyinxu5 x4uap5 x1g2khh7 xkhd6sd"]').text
       
        print("Analizando elemento", texto_descripcion)
        print(url)
       
        imagen_elemento = driver.find_element(By.XPATH, '//img[@class="x85a59c x193iq5w x4fas0m x19kjcj4"]')
        
      
        url_imagen = imagen_elemento.get_attribute('src')
        
        nombre_imagen = hashlib.sha256(bytes(url_imagen, 'utf-8')).hexdigest()
       
        elementos_capturados.append([nombre_imagen, texto_descripcion, url_imagen])
        
        
        #urllib.request.urlretrieve(url_imagen, nombre_imagen)
        urllib.request.urlretrieve(url_imagen, f'/Users/datos-lc/Documents/Colecciones ongoing/jalisco/{nombre_imagen}.jpeg')
        
        
    except NoSuchElementException:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("                                                                  ")
        print("no lo pudimos encontrar", url)
        
        elementos_faltantes.append([nombre_imagen, url_imagen])
        
        

    driver.quit()
    return elementos_capturados, elementos_faltantes
    contador += 1
    
for i in range(len(urls)):
   enter_url(urls[i])

#screenshots = Parallel(n_jobs=-1, prefer="threads")(delayed(enter_url)(urls[url])  for url in range(len(urls)))



df_falt = pd.DataFrame(elementos_faltantes)
df_falt.to_csv("/Users/datos-lc/Documents/Colecciones ongoing/jalisco/faltantes.csv", index=False)
df_falt = pd.DataFrame(elementos_capturados)
df_falt.to_csv("/Users/datos-lc/Documents/Colecciones ongoing/jalisco/capturados.csv", index=False)
#screenshots = Parallel(n_jobs=-1)(delayed(enter_url)(urls[url]) for url in range(len(urls)))

#print(screenshots)
#df_capt = pd.DataFrame(screenshots)
#df_capt.to_csv("capturados.csv", index=False)




#df_screen = pd.DataFrame(screenshots)
#df_screen.to_csv('/Users/datos-lc/Documents/Colecciones ongoing/Baja_california/screen.csv', index=False)
#df_falt = pd.DataFrame(elementos_faltantes)
#df_falt.to_csv("/Users/datos-lc/Documents/Colecciones ongoing/Baja_california/faltantes.csv", index=False)
#df_falt = pd.DataFrame(elementos_capturados)
#df_falt.to_csv("/Users/datos-lc/Documents/Colecciones ongoing/Baja_california/capturados.csv", index=False)



