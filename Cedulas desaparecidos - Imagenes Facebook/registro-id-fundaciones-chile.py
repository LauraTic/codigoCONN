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


driver = webdriver.Firefox()
driver.get("https://rpjweb.srcei.cl/RPJ/Consulta/apps/consulta_lista_rpj.php")
time.sleep(50)

data = []
input = driver.find_element(By.XPATH, "//input[@id='rpj_p1']")

input.send_keys('165722')

time.sleep(3)

boton = driver.find_element(By.XPATH, "//button[@id='btnrpj_p1']")

boton.click()

informacion = boton = driver.find_elements(By.XPATH, "//table[@id='resultadostb']/tbody/tr/td")

print(len(informacion))

print(informacion)

rut = sanitizar_texto(informacion[0].text) 
num = sanitizar_texto(informacion[1].text)
name = sanitizar_texto(informacion[2].text)
fecha = sanitizar_texto(informacion[3].text)
comuna = sanitizar_texto(informacion[4].text)
enlace = informacion[-1].find(By.TAG_NAME, "a").get_attribute('href')

datos = {
    'RUT': rut,
    'Num': num,
    'Nombre': name,
    'Fecha': fecha,
    'Comuna': comuna,
    'Enlace': enlace
}
print(datos)

data.append(datos)
print(data)





