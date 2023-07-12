import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import pandas as pd
import os
import string
import urllib.request
import time

def reed_excel(ruta):
    df = pd.read_excel(ruta)
    enlace_proceso = df['enlace']
    enlace_proceso.to_list()
    print(len(enlace_proceso))
    return enlace_proceso

def sanitize_filename(filename):
    filename_edited = filename.replace("/", "-")
    return filename_edited

def status_code_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        s = BeautifulSoup(r.text, 'lxml')
        return s
    else:
        print('Error: El código de estado no es correcto')
        return None


def completar_url(url):
    url_base='https://compranet.hacienda.gob.mx'
    return urljoin(url_base, url)

def encontrar_documentos(url):
    ruta_guardado = '/Users/datos-lc/Documents/Colecciones ongoing/SEDENA/Documentos_completos/'

    print("Proceso actual: ")
    print(url)
    
    s = status_code_url(url)
    if s is None:
        print("enlace del proceso tiene error")
        return
    
    name_proceso = sanitize_filename(s.find('div', {'class': 'subtitle_01 maintitle'}).text.strip())

    pdf = s.find_all('div', {'class': 'attachTag_left'}) #Encontrar los contenedores de los documentos del proceso
    parrafos = s.find_all('h3', {'class': 'paragraph'}) #Encontrar si hay tabla de anexos
    pattern = "\/([^']+)'" #Traer el enlace de los documentos del proceso.
    for i in pdf:
        onclick = i.find('a').get('onclick')
        print(onclick)
        match = re.search(pattern, onclick)
        print(match)
        if match:
            url = completar_url(match.group(1))
            print("Soy la url del documento del proceso")
            print(url)
            nombre = sanitize_filename(i.find('a').get('title').replace("Descargar archivo adjunto: ", "").strip())
            nombre_archivo = name_proceso + " - " + nombre

            if len(nombre_archivo) > 250:
                expediente = name_proceso[:20]
                nombre_archivo = expediente + " " + nombre

            ruta_archivo = os.path.join(ruta_guardado, nombre_archivo)
            """try:
                download_file(url, ruta_archivo)
            except Exception as e:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Se produjo un error al descargar el archivo anexo:", str(e))
                continue"""
    
    
    anexos = [i for i in parrafos if "Anexos" in i.text] #Guardar el h3 si este tiene nombre anexos, es solo para comprobar, no tiene otra función
    """if anexos:
        print("Tiene anexo")
        tabla_anexo = s.find_all('table')[-1]
        enlaces = tabla_anexo.find_all('a', href=True)
        if enlaces:
            for enlace in enlaces:
                href = completar_url(enlace['href'])
                texto = sanitize_filename(enlace.get('title').replace("Descargar archivo adjunto: ", "").strip())
                print(href)
                nombre_anexo = name_proceso + " - " + texto
                ruta_anexo = os.path.join(ruta_guardado, nombre_anexo)
                try:
                    download_file(href, ruta_anexo)
                except Exception as e:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Se produjo un error al descargar el archivo anexo:", str(e))
                    continue"""

            
  
def download_file(url, ruta):
    headers = {
        
        "Cookie": "VISITORID=3cccd793-6862-4c1a-bace-e1a24b72452d"
        #"Cookie": "JSESSIONID=v_jmoUayZclEUPRgMWM1DOKomuvuR39Bqhkz8kvs.sfpadm_lb2; VISITORID=22d441e5-0046-47e0-8477-98a6af20d749; _gid=GA1.3.130702762.1687905976; _gat_gtag_UA_141511568_1=1; _ga_G91L64PNVG=GS1.1.1687905976.7.0.1687905976.0.0.0; _ga=GA1.1.2004777467.1677274213; VISITOR_ET=22d441e5%3A1687906885184; _tabSessionId=1d4609ac-6021-f4ab-2811-fe2d7b91cdd1" 
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    with open(ruta, 'wb') as file:
        file.write(response.read())
    print("Completed")
     


if __name__=='__main__':
    #lista_enlaces = reed_excel("/Users/datos-lc/Documents/Colecciones ongoing/SEDENA/2019.xlsx")
    #encontrar_documentos("https://compranet.hacienda.gob.mx/esop/guest/go/opportunity/detail?opportunityId=1669456")
    encontrar_documentos("https://compranet.hacienda.gob.mx/esop/guest/go/opportunity/detail?opportunityId=2077944")
    """enlaces_descargados = []
    for i in lista_enlaces:
        try:
            enlaces_descargados.append(encontrar_documentos(i))
            time.sleep(10)
        except Exception as e:
            print("Se produjo un error en el enlace:", str(e))
            continue"""
    
        # Exportar a Excel
    """df = pd.DataFrame(enlaces_descargados, columns=['Enlace Descargado'])
    df.to_excel('enlaces_descargados.xlsx', index=False)"""

        

    

    """req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)            
    nombre_archivo = name_proceso + " - " + nombre
    try:
        if len(nombre_archivo) > 250:
            expediente = name_proceso[:20]
            nombre_archivo = expediente + " " + nombre

        ruta_archivo = os.path.join(ruta_guardado, nombre_archivo)
        with open(ruta_archivo, 'wb') as file:
            file.write(response.read())
        time.sleep(10)
    except Exception as e:
                print("Se produjo un error al descargar el archivo del proceso:", str(e))"""
                
                

    
    """try:
                reque = urllib.request.Request(href, headers=headers)
                nombre_anexo = name_proceso + " - " + texto
                ruta_anexo = os.path.join(ruta_guardado, nombre_anexo)

                with open(ruta_anexo, 'wb') as file:
                    file.write(response.read())
                time.sleep(10)
            except Exception as e:
                print("Se produjo un error al descargar el archivo anexo:", str(e))
                continue"""