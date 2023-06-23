import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import os
import pandas as pd

df = pd.read_excel("/Users/datos-lc/Downloads/tribunal-segundo-demandas.xlsx")

for name, enlace in zip(df['nombre'],df['enlace']):

        r = requests.get(enlace)
        parsed_url = urlparse(enlace)
        filename = os.path.basename(parsed_url.path)
        file_path = f'/Users/datos-lc/Documents/Colecciones ongoing/Segundo tribunal/demandas/{name} {filename}'

        with open(file_path, 'wb') as f:
                f.write(r.content)