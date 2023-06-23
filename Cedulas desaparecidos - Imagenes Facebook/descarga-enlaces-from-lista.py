import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import os


url_sentencias = 'https://tribunalambiental.cl/sentencias-e-informes/sentencias/#'

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
    tipos_sancion=["Reclamaciones","Demandas", "Consultas", "Solicita"]
    links_sanciones=s.find_all('li')

    for i in links_sanciones:
       for y in tipos_sancion:
           if y in i.text:
            enlaces.append(i.find('a').get('href'))
    print(enlaces)
    return enlaces

"""def links_anios(s):
    h5_year=s.find_all('h5')
    url_list=[completar_url(x.find('a').get('href')) for x in h5_year]
    return url_list
"""
def links_pdf(url):
    enlaces_pdf = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        enlaces_s = soup.find_all('a')
        #nombres_s = soup.find_all('b')
        #count = 0

        url_list = [x.get('href') for x in enlaces_s]
        
        print(url_list)
        print(len(url_list))

        """ for i in url_list:
            if i is not None and i.endswith('pdf'):
                print(i)
                print(nombres[count])
                count +=1
                print(count)
                r = requests.get(i)
                parsed_url = urlparse(i)
                filename = os.path.basename(parsed_url.path)
                file_path = f'/Users/datos-lc/Documents/Colecciones ongoing/Tribunal tercero/{filename}'
                with open(file_path, 'wb') as f:
                        f.write(r.content)"""
   


        """for i in enlaces_s:
            nombre = i.find('b').text
            enlaces = i.find_all('a')
            for y in enlaces:               
                enlaces_pdf.append(y.get('href'))"""

    """for guardar in enlaces_pdf:
                if guardar is not None and guardar.endswith('pdf'):
                    r = requests.get(guardar)
                    parsed_url = urlparse(guardar)
                    filename = os.path.basename(parsed_url.path)
                    file_path = f'/Users/datos-lc/Documents/Colecciones ongoing/Sentencias Tribunal 3/Fallos/{nombre} - {filename}'

                    with open(file_path, 'wb') as f:
                        f.write(r.content)"""

    """print(enlaces_pdf)
            print(nombre)
"""

if __name__ == '__main__':
    s = status_code_url(url_sentencias)
    #links_tipo_sancion()
    print(s)
    
    #links_pdf('')
    #enlaces_sanciones = links_tipo_sancion(s)
    #for i in enlaces_sanciones:
     #   links_pdf(i)

    """for x in enlaces_pdf:
        enlaces_pdf_guardar.append(x)  """

    """ i = 0
        while i < len(enlaces_pdf_guardar):  
            
            print(f'Estoy descargando el enlace {i}', enlaces_pdf_guardar[0])
            save_in_disk(enlaces_pdf_guardar[i], i)
            i += 1 """

    