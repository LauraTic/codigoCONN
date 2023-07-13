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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



##########  Código para hacer scroll hasta abajo y guardar las URLS de las imágenes de las cédulas en Facebook #########
# Configurar el navegador y cargar la página web
pagina_web = 'https://www.facebook.com/BusquedaJal/photos'
#driver = webdriver.Chrome(ChromeDriverManager().install())


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(pagina_web)

# Esperar un tiempo para que la página cargue completamente
time.sleep(3)

# Desplazar la página gradualmente y capturar elementos
scroll_incremento = 500  # Incremento de desplazamiento en píxeles
scroll_actual = 500  # Posición de desplazamiento actual

scrolled = 0 


while scrolled < 12000:
    driver.execute_script(f"window.scrollTo(0, {scroll_actual});")
    time.sleep(0.5)
    scroll_actual += scroll_incremento
    scrolled += 1

elementos = driver.find_elements(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1lliihq x5yr21d x1n2onr6 xh8yej3"]')


cantidad_elementos = len(elementos)
print("##########################################################################################")
print("##########################################################################################")
print("                                                                                                ")
print("LA CANTIDAD DE ELEMENTOS CAPTURADOS SON: ", cantidad_elementos)


for elemento in elementos:
    href = elemento.get_attribute('href')
    urls.append(href)

df_url = pd.DataFrame(urls, columns=['URL'])
df_url.to_csv("/Users/datos-lc/Documents/Colecciones ongoing/jalisco/url-jalisco.csv", index=False)
