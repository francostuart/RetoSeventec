import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_correo_gmail(output, destinatario):
    # Configuración de la cuenta y del servidor
    direccion_email = "francostuart95@gmail.com"
    password = "jbum vixq sdcz hyhl"
    servidor_smtp = "smtp.gmail.com"
    puerto = 587

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = direccion_email
    msg['To'] = destinatario
    msg['Subject'] = "testSeventec"
    msg.attach(MIMEText("Envio correo adjuntado la boleta", 'plain'))

    # Adjuntar el archivo
    parte = MIMEBase('application', 'octet-stream')
    with open(output, 'rb') as archivo:
      parte.set_payload(archivo.read())
    encoders.encode_base64(parte)
    parte.add_header(
        'Content-Disposition',
        f'attachment; filename={output}',
    )
    msg.attach(parte)

    # Conectar al servidor python -m pip install pywin32
    server = smtplib.SMTP(servidor_smtp, puerto)
    server.starttls()  # Activar la seguridad
    server.login(direccion_email, password)

    # Enviar el correo
    server.send_message(msg)
    server.quit()

    return True

# Ejemplo
#enviar_correo_gmail('francostuart95@gmail.com', 'Asunto del Mensaje', 'Este es el cuerpo del mensaje.')