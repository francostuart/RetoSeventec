RPA Autoconsolidador de boletas, consolida la informacion extraida de las boletas en un pdf.
El bot intera y lee las boletas con formarto txt, estas deben estar almacenadas en la carpeta Input
Genera un pdf de todos los txt capturados y lo almacena en carpeta Output
Posterior a ello envia correo con el pdf adjuntado (gmail smtp).


(Los destinatarios se pueden configurar en el ./Robot/Config.txt al igual que las rutas)
El robot registra un log de auditoria del proceso que se almacena en la carpeta Logs

Prerequisitos
Debe tener instalado lo sgt:
	Python 3.9
	Al clonar el proyecto respetar la estructura de carpeta:(C:/RPA_SEVENTEC_PY), en caso que se cambie la ruta, las rutas del robot se deben configurar en el Config.txt

Ejecucion:

Clone el proyecto, y ejecute el Main.bat que esta en la carpeta principal, para ejecutar la automatizacion.
isntalar las librerias indicadas en requeriments.txt, puede utilizar el comando: pip install -r requirements.txt


