from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER

# Nombre del archivo de texto y del PDF de salida
nombre_archivo_txt = 'documento.txt'
nombre_archivo_pdf = 'documento.pdf'

# Crear un objeto canvas para dibujar el PDF
c = canvas.Canvas(nombre_archivo_pdf, pagesize=LETTER)
width, height = LETTER  # Tamaño de la página

# Abrir el archivo de texto y leer las líneas
with open(nombre_archivo_txt, 'r') as archivo_txt:
    lineas = archivo_txt.readlines()

# Coordenadas iniciales para la primera línea
x = 72  # Margen izquierdo
y = height - 72  # Margen superior

for linea in lineas:
    # Dibujar la línea en el PDF
    c.drawString(x, y, linea.strip())
    y -= 12  # Disminuir el valor de y para moverse hacia abajo en el PDF

    # Si hemos llegado al final de la página, crear una nueva
    if y < 72:
        c.showPage()
        y = height - 72  # Restablecer el margen superior

# Guardar el PDF
c.save()