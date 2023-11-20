from datetime import datetime


def leerConfig(ruta_config):
    variables = {}   # Diccionario que contendra los datos leidos.
    print(ruta_config)
    try:
        with open(ruta_config, "r") as datos:
            for linea in datos:
                nombre, valor = linea.strip().split("=", maxsplit=1)
                variables[nombre] = valor
    except Exception as e:
            print("Error al leer config: " + str(e))
            return False
    return variables

