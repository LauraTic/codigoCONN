import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import os


url_sentencias = 'https://www.3ta.cl/fallos/'

def status_code_url(url):
    r = requests.get(url)
    print(r.status_code)
    if r.status_code==200:
        s=BeautifulSoup(r.text, 'lxml')
    else:
        print('error no es correcto el status')
    return s


def links_tipo_sancion(s):
    enlaces=[]
    tipos_sancion=["Reclamaciones","Demandas ", "Solicitudes","Consultas","Inadmisibilidades", "Conciliaciones"]
    links_sanciones=s.find_all('li')

    for i in links_sanciones:
       for y in tipos_sancion:
           if y in i.text:
            enlaces.append(i.find('a').get('href'))
    return enlaces

"""def links_anios(s):
    h5_year=s.find_all('h5')
    url_list=[completar_url(x.find('a').get('href')) for x in h5_year]
    return url_list
"""
def links_pdf(url):
    enlaces_pdf = []
    s = status_code_url(url)
    enlaces_s = s.find_all('a')
    links = [x.get('href') for x in enlaces_s if x is not None]
    for link in links:
        if link is not None and link.endswith('pdf'):
            enlaces_pdf.append(link)
    return enlaces_pdf

def save_in_disk(url, i):
    r = requests.get(url)
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    with open(f'/Users/datos-lc/Documents/Colecciones ongoing/Sentencias Tribunal 3/Fallos/{filename}', 'wb') as f:
        f.write(r.content)


def completar_url(url):
    url_base='https://www.3ta.cl/'
    return urljoin(url_base, url)

if __name__ == '__main__':
    s = status_code_url(url_sentencias)
    enlaces_sanciones = links_tipo_sancion(s)
    enlaces_pdf_guardar = []
    enlaces_pdf = links_pdf("https://3ta.cl/fallos/")

    for x in enlaces_pdf:
        enlaces_pdf_guardar.append(x)  

    i = 0
    while i < len(enlaces_pdf_guardar):  
        
        print(f'Estoy descargando el enlace {i}', enlaces_pdf_guardar[0])
        save_in_disk(enlaces_pdf_guardar[i], i)
        i += 1 

    