
import requests

url = "https://compranet.hacienda.gob.mx/esop/guest/go/opportunity/detail?opportunityId=1622447"
response = requests.get(url)

print(response.headers)






"""import requests

url = "https://compranet.hacienda.gob.mx/esop/toolkit/DownloadProxy/41424330?verify=13&oid=39218488"  # Reemplaza con la URL deseada

response = requests.get(url)
cookies = response.cookies
print("Estas son las cookies")
print(cookies)

# Nombres de las cookies que deseas obtener
cookie_names = ["VISITORID", "VISITOR_ET", "_ga_G91L64PNVG", "_ga_ZTH7FZZTGF", "_ga", "_tabSessionId"]

# Imprimir los nombres de todas las cookies presentes en la respuesta
for cookie in cookies:
    print("Estas son las cookies name")
    print(cookie.name)

cookie_values = {}
for cookie in cookies:
    if cookie.name in cookie_names:
        cookie_values[cookie.name] = cookie.value

# Construir el diccionario headers con los valores de las cookies
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cookie": "; ".join([f"{name}={value}" for name, value in cookie_values.items()])
}
print("Estas son los")
print(headers)
"""








"""import requests

url = "https://compranet.hacienda.gob.mx/esop/toolkit/DownloadProxy/41424330?verify=13&oid=39218488"  # Reemplaza con la URL deseada

response = requests.get(url)
cookies = response.cookies
print("Hola")
print(response)
print(cookies)

for cookie in cookies:
    print(cookie.name, cookie.value)"""

"""
import requests

def main():
    url = "https://compranet.hacienda.gob.mx/esop/toolkit/DownloadProxy/41424330?verify=13&oid=39218488"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookies": "JSESSIONID=D276kZtTQpg6w7oWQYEaJfFWtVOlSFZJFk1A60Wv.sfpadm_lb1"
    }
    download_file(url, headers)

    cookies = get_cookies(url)
    if cookies:
        headers["Cookie"] = cookies
        print(cookies)

    

def get_cookies(url):
    response = requests.get(url)
    cookies = response.cookies.get_dict()
    cookie_string = "; ".join([f"{name}={value}" for name, value in cookies.items()])
    return cookie_string

def download_file(url, headers):
    response = requests.get(url, headers=headers)
    with open("document.pdf", 'wb') as file:
        file.write(response.content)
    print("Completed")

if __name__ == "__main__":
    main()"""
"""
import urllib.request

def main():
    url = "https://compranet.hacienda.gob.mx/esop/toolkit/DownloadProxy/41531633?verify=13&oid=39340470"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookies": "JSESSIONID=D276kZtTQpg6w7oWQYEaJfFWtVOlSFZJFk1A60Wv.sfpadm_lb1; _ga=GA1.1.339374753.1686073501; _ga=GA1.4.339374753.1686073501; _ga_G91L64PNVG=GS1.1.1686073500.1.1.1686073720.0.0.0; _ga_ZTH7FZZTGF=GS1.1.1686073521.1.1.1686073843.0.0.0; VISITORID=23458237-b58c-4f55-965e-4fab52cbb8c0; VISITOR_ET=23458237%3A1687885491891; _tabSessionId=c73a10a1-2d4a-b159-9e27-1d2ce5495ae0"
    }
    download_file(url, headers)

def download_file(url, headers):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    with open("document.pdf", 'wb') as file:
        file.write(response.read())
    print("Completed")

if __name__ == "__main__":
    main()"""
