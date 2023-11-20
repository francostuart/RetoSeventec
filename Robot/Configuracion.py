import os
from datetime import datetime
from lectura import *

#declaracion de variables
ruta_input = ""
ruta_output = ""



#Obtiene el consolidado del contenido de las boletas de entrada
def configuracionInicial(ruta_config):
    
    #leer config para obtener las rutas de entrada del proceso
    rutas_entrada = leerConfig(ruta_config)
    
    #validar si la funcion leerConfig devolvio un error
    if not rutas_entrada:
        print("Error al leer config")
        return False
    
    ruta_input = rutas_entrada['ruta_input']
    ruta_output = rutas_entrada['ruta_output'] + "Boletas.pdf"
    correo_destino = rutas_entrada['correo_destino']
    correo_copia = rutas_entrada['correo_copia']
    
   
    
    #inicializar bandera de funcion
    estado = False
    text_boletas = ""
    
    #Fecha actual
    now = datetime.now()
    now = now.strftime("%m.%d.%Y_%H.%M.%S")
    


    #asignar diccionario de rutas del proceso obtenidas
    rutas = {'ruta_input': ruta_input, 'ruta_output': ruta_output, 'correo_destino': correo_destino, 'correo_copia': correo_copia}
    

    #Leer contenido del config
    with open(ruta_config) as f:
        contenido = f.read()

    #Obtener boletas de la carpeta input
    with os.scandir(ruta_input) as boletas:
        boletas = [boleta.name for boleta in boletas if boleta.is_file() and boleta.name.startswith('Boleta') and boleta.name.endswith('.txt')]
    
    if len(boletas) < 1:
        return 2

    #Obtener contenido de cada boleta y se consolida en una variable
    for boleta in boletas:
        with open(ruta_input + boleta, encoding='utf-8') as f:
            contenido = f.read()
            text_boletas = text_boletas + contenido

   
    estado = True
    return estado, text_boletas, rutas


