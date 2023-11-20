RPA Autoconsolidador de boletas, consolida la informacion extraida de las boletas en un pdf.
El bot intera y lee las boletas con formarto txt, estas deben estar almacenadas en la carpeta Input
Genera un pdf de todos los txt capturados y lo almacena en carpeta Output
Posterior a ello envia correo con el pdf adjuntado (gmail smtp).

Ejecucion:
Tener en cuenta que se debe eliminar el archivo boletas.pdf, antes de ejecutar la automatizacion.
Clonar el proyecto y ejecutar el Main.bat.
Instalar las librerias indicadas en requeriments.txt.

Prerequisitos
Debe tener instalado lo sgt:
	Python 3.9
	Al clonar el proyecto debe tener la estructura de carpeta:"C:/RPA_SEVENTEC_PY" como carpeta principal, en caso que se cambie la ruta, las rutas del robot se deben configurar en el Config.txt



