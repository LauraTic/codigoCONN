import time
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request

# Configurar el navegador y cargar la página web
pagina_web = 'https://www.facebook.com/BusquedaJal/photos'
driver = webdriver.Chrome()
driver.get(pagina_web)

# Obtener el número inicial de imágenes
elementos = driver.find_elements(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1lliihq x5yr21d x1n2onr6 xh8yej3"]//img')
num_imagenes = len(elementos)

# Realizar scroll hasta que se carguen todas las imágenes
while True:
    # Desplazarse hacia abajo en la página
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    
    # Esperar un momento para que se carguen las imágenes
    time.sleep(2)  # Ajusta el tiempo según sea necesario
    
    # Obtener el número actual de imágenes
    elementos = driver.find_elements(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1lliihq x5yr21d x1n2onr6 xh8yej3"]//img')
    num_imagenes_actual = len(elementos)
    
    # Si no hay más imágenes por cargar, salir del bucle
   # if num_imagenes_actual == num_imagenes:
        #break
    
    # Actualizar el número de imágenes
    num_imagenes = num_imagenes_actual

# Iterar sobre cada imagen y realizar las operaciones necesarias
"""for i, elemento in enumerate(elementos):
    # Haz clic en la imagen para interactuar con ella
    elemento.click()

    # Realiza las operaciones necesarias con la imagen actual
    # por ejemplo, puedes obtener la URL de la imagen:
    url_imagen = elemento.get_attribute('src')
    print("Imagen", i+1, "URL:", url_imagen)

    # Vuelve a la página anterior o realiza otras operaciones
    driver.back()"""
