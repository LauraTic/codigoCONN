import pandas as pd
from openpyxl import load_workbook

path = '/Users/datos-lc/Documents/Colecciones ongoing/cedulas-jalisco/Cédulas.xlsx'
df = pd.read_excel(path)

partes = [df[i:i+1000] for i in range(0, len(df), 1000)]

# Guarda cada parte en un archivo Excel separado
for i, parte in enumerate(partes):
    parte.to_excel(f'/Users/datos-lc/Documents/Colecciones ongoing/cedulas-jalisco/parte_{i+1}.xlsx', index=False)





    

