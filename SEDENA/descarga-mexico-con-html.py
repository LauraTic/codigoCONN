import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re



def status_code_url(url):
    r=requests.get(url)
    
    if r.status_code==200:
        s=BeautifulSoup(r.text, 'lxml')
    else:
        print('error no es correcto el status')
    return s


def completar_url(url):
    url_base='https://compranet.hacienda.gob.mx/'
    return urljoin(url_base, url)

def encontrar_pdf_procedimiento(url):
    s = status_code_url(url)
    name = s.find('div',{'class':'subtitle_01 maintitle'})
    pdf = s.find_all('div', {'class': 'attachTag_left'})
    go_to_url = [i.find('a').get('onclick') for i in pdf]
    pattern = "gotoUrl\('/(.*?)'\)"
    regex = [re.search(pattern, x) for x in go_to_url]
    url_enlaces_descarga = [completar_url(y.group(1))for y in regex]
    anexos = s.find_all('h3', {"class": "paragraph"})
    anexos_enlace = []
    count = 0
    for i in anexos:
        verificar = i.text
        if "Anexos" in verificar:
            count +=1           
            print(verificar)
        else:
            print("No tiene anexo")
    
    if count > 0:
        enlace = completar_url(s.find_all('a'))
        for i in enlace:
            anexos_enlace.append(i.get('href'))
        
    print(anexos_enlace)
    
    pdf_enlace = []
    
    
    return

def guardar(enlace, name):
    return


if __name__=='__main__':

    s = encontrar_pdf_procedimiento('https://compranet.hacienda.gob.mx/esop/guest/go/opportunity/detail?opportunityId=1955614')
    #encontrar_pdf_procedimiento(s)


