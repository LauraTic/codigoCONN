#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import wget
import os


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
path = '/Users/datos-lc/Documents/Colecciones ongoing/cedulas-jalisco/'

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

time.sleep(5)
images = [] 
texto = []
diccionario = {}

driver.get("https://www.facebook.com/BusquedaJal/photos")
time.sleep(5)

for j in range(0,350):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

anchors = driver.find_elements(By.TAG_NAME, 'a')
anchors = [a.get_attribute('href') for a in anchors]
anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
print('Found ' + str(len(anchors)) + ' links to images')

df_url = pd.DataFrame(anchors, columns=['URL'])
df_url.to_csv("/Users/datos-lc/Documents/Colecciones ongoing/cedulas-jalisco/lista_urls.csv", index=False)
counter = 0
for a in anchors:
    driver.get(a)
    time.sleep(5)
    img = driver.find_elements(By.TAG_NAME, "img")
    image = img[0].get_attribute("src")
    print(image)
    name = driver.find_element(By.XPATH, "//div[@class='xyinxu5 x4uap5 x1g2khh7 xkhd6sd']")
    name = name.text
    save_as = os.path.join(path, str(counter) + '.jpg')
    wget.download(image, save_as)
    time.sleep(5)
    diccionario[counter] = {'Imagen': str(counter) + '.jpg', 'Texto': name}
    counter += 1

df = pd.DataFrame.from_dict(diccionario, orient='index')
ruta = os.path.join(path, "diccionario.xlsx")
df.to_excel(ruta, index=False)
print('I scraped ' + str(counter) + ' images!')

