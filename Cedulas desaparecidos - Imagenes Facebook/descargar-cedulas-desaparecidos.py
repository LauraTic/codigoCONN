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
pagina_web = 'https://www.facebook.com/bc.cebp/photos_by'
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
urls = []  # Lista para almacenar los detalles de cada elemento
scrolled = 0 
elementos_capturados = []
elementos_faltantes = []


while scrolled < 3000:
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
df_url.to_csv("/Users/datos-lc/Documents/Colecciones ongoing/Baja_california/lista_urls.csv", index=False)

contador = 0

def enter_url(url):
    global contador, elementos_capturados, elementos_faltantes, driver

    WebDriverWait(driver, 10).until(EC.url_to_be(url))
    
    driver.get(url)

    time.sleep(5)
    

    try:
        texto_descripcion = driver.find_element(By.XPATH, '//div[@class="xyinxu5 x4uap5 x1g2khh7 xkhd6sd"]').text
       
        print("Analizando elemento", texto_descripcion)
       
        imagen_elemento = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
            By.XPATH, '//img[@class="x85a59c x193iq5w x4fas0m x19kjcj4"]'))
        
      
        url_imagen = imagen_elemento.get_attribute('src')
        
        nombre_imagen = hashlib.sha256(bytes(url_imagen, 'utf-8')).hexdigest()
       
        elementos_capturados.append([nombre_imagen, texto_descripcion, url_imagen])
        
        
        #urllib.request.urlretrieve(url_imagen, nombre_imagen)
        urllib.request.urlretrieve(url_imagen, f'/Users/datos-lc/Documents/Colecciones ongoing/Baja_california/{nombre_imagen}.jpeg')
        
        
    except NoSuchElementException:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("                                                                  ")
        print("no lo pudimos encontrar", url)
        
        elementos_faltantes.append([nombre_imagen, url_imagen])
        df_falt = pd.DataFrame(elementos_faltantes)
        df_falt.to_csv("/Users/datos-lc/Documents/Colecciones ongoing/Baja_california/faltantes.csv", index=False)


    return elementos_capturados, elementos_faltantes
    contador += 1


screenshots = Parallel(n_jobs=-1)(delayed(enter_url)(url) for url in urls)

df_screen = pd.DataFrame(screenshots)
df_screen.to_csv('/Users/datos-lc/Documents/Colecciones ongoing/Baja_california/screen.csv', index=False)





