import os
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
import requests
import bs4
from bs4 import BeautifulSoup
import unicodedata


 
def sanitizar_texto(texto):
    texto_sin_tildes = ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))
    return texto_sin_tildes

def reed_text(enlace):
    
    driver = webdriver.Chrome()
    driver.get(enlace)
    url_list = []
    url_fundaciones_list = []

    for i in range(12):

        celdas = driver.find_elements(By.XPATH, "//td[@class='celdaMantenedor izquierda']/a")
        
        for i in range(len(celdas)):
            url_list.append(celdas[i].get_attribute('href'))


        imagenes = driver.find_elements(By.XPATH, "//div[@class='medio']/a")
        boton_siguiente = imagenes[6]
        actions = ActionChains(driver)
        actions.click(boton_siguiente)
        actions.perform()
        time.sleep(3)
    
    print(len(url_list))


    for y in range(len(url_list)):
            if url_list[y].endswith("5"):
                url_fundaciones_list.append(url_list[y])
    
    print(url_fundaciones_list)
    print(len(url_fundaciones_list))
    return url_fundaciones_list              


data = [] 


def fichas(url):

    driver = webdriver.Chrome()
    driver.get(url)
    textos = driver.find_elements(By.XPATH, "//div[@class='label negrita']")
    print(len(textos))

    rut = sanitizar_texto(textos[0].text) 
    nombre = sanitizar_texto(textos[1].text)
    tipo_institucion = sanitizar_texto(textos[3].text)
    numero = sanitizar_texto(textos[8].text)

    datos = {
        'RUT': rut,
        'Nombre': nombre,
        'Tipo': tipo_institucion,
        'Num': numero
    }
    print(datos)

    data.append(datos)
    print(data)
    driver.quit()


lista_enlaces_fundaciones = reed_text('https://www.registros19862.cl/reportes/transferencias/reporte/ingresadas?pagina=1&WHERE%5Btransferencia%5D%5Btipo_fecha%5D=0&WHERE%5Btransferencia%5D%5Bfecha_desde%5D=&WHERE%5Btransferencia%5D%5Bfecha_hasta%5D=&WHERE%5Btransferencia%5D%5Brut_donante%5D=61.930.500-0&WHERE%5Btransferencia%5D%5Bnombre_donante%5D=&WHERE%5Btransferencia%5D%5Brut_receptor%5D=&WHERE%5Btransferencia%5D%5Bnombre_receptor%5D=&WHERE%5Btransferencia%5D%5Bagrupar%5D=0') 

#fichas('https://www.registros19862.cl/fichas/ver/rut/65080066/clase/5')

for i in lista_enlaces_fundaciones:
    fichas(i)
    
df = pd.DataFrame(data)
print(df)
df.to_csv('/Users/datos-lc/Documents/Prueba/datos.csv', index=False)




