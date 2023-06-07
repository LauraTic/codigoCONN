import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request

# Configurar el navegador y cargar la página web
pagina_web = 'https://www.facebook.com/BusquedaJal/photos'
driver = webdriver.Chrome()
driver.get(pagina_web)

# Esperar un tiempo para que la página cargue completamente
time.sleep(3)

# Desplazar la página gradualmente y capturar elementos
total_elementos = 0
scroll_incremento = 500  # Incremento de desplazamiento en píxeles
scroll_actual = 500  # Posición de desplazamiento actual
elementos_capturados = []  # Lista para almacenar los detalles de cada elemento

while True:
    # Desplazar la página hacia abajo
    driver.execute_script(f"window.scrollTo(0, {scroll_actual});")
    time.sleep(1)
    scroll_actual += scroll_incremento

    # Capturar los elementos visibles actualmente
    elementos = driver.find_elements(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1lliihq x5yr21d x1n2onr6 xh8yej3"]')
    cantidad_elementos = len(elementos)
    print(cantidad_elementos)

    # Verificar si se cargaron nuevos elementos
    if cantidad_elementos > total_elementos:
        total_elementos = cantidad_elementos

        for elemento in elementos:
            detalle_elemento = {}

            # Hacer clic en el elemento
            elemento.click()
            time.sleep(5)

            # Cerrar la ventana emergente
            cerrar_elemento = driver.find_element(By.XPATH, '//div[@aria-label="Cerrar"]')
            cerrar_elemento.click()
            time.sleep(3)
    else:
        
        print("Soy un else cuando cantidad de elementos no aumenta y es igual a total elementos")
        break

"""# Imprimir la cantidad de elementos capturados
print("Total de elementos capturados:", total_elementos)

# Imprimir los detalles de cada elemento capturado
for i, elemento in enumerate(elementos_capturados):
    print(f"Elemento {i+1}:")
    print("Imagen:", elemento['imagen'])
    print("Descripción:", elemento['descripcion'])
    print()

# Cerrar el navegador y finalizar el código
driver.quit()
"""