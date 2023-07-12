import pandas as pd
from fpdf import FPDF

# Crear DataFrame de ejemplo
data = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
        'Edad': [25, 30, 35, 28],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}
df = pd.DataFrame(data)

# Crear una clase personalizada basada en FPDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Encabezado del PDF', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')

# Crear una instancia del objeto PDF
pdf = PDF()
pdf.add_page()

# Configurar opciones
pdf.set_font('Arial', 'B', 12)
pdf.cell(40, 10, 'Nombre', 1)
pdf.cell(40, 10, 'Edad', 1)
pdf.cell(40, 10, 'Ciudad', 1)
pdf.ln()

pdf.set_font('Arial', '', 12)
for index, row in df.iterrows():
    pdf.cell(40, 10, str(row['Nombre']), 1)
    pdf.cell(40, 10, str(row['Edad']), 1)
    pdf.cell(40, 10, str(row['Ciudad']), 1)
    pdf.ln()

# Guardar el archivo PDF
pdf.output('archivo.pdf')
