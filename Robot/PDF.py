import aspose.pdf as aspose_pdf
import os.path
from lectura import *

def generar_documento_pdf(contenido_texto, ruta_salida):
    # Declaración de variables de proceso
    exito = False
    intentos = 0
    maximo_intentos = 3

    # Flujo con reintentos en caso de error
    while intentos < maximo_intentos:
        try:
            intentos += 1

            # Inicialización del objeto tipo documento PDF
            documento_pdf = aspose_pdf.Document()

            # Se agrega una nueva página al documento
            pagina = documento_pdf.pages.add()

            # Inicialización de un área de texto
            area_texto = aspose_pdf.text.TextFragment(contenido_texto)

            # Se agrega el área de texto a la página
            pagina.paragraphs.add(area_texto)

            # Se exporta y guarda el PDF en la ruta especificada como parámetro
            documento_pdf.save(ruta_salida)
            exito = True
        except Exception as error:
            # Se maneja la excepción y se continua con el siguiente intento si hay error
            continue

    return exito
