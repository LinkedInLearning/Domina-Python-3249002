import os
import smtplib

from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")


def enviar_email():

    receptor = "xeunnannoibeumau-6316@yopmail.com"
    email = EmailMessage()

    email["From"] = SENDER_EMAIL
    email["To"] = receptor
    email["Subject"] = "Correo desde Python"
    mensaje = "Prueba de envío de correo desde Python"
    email.set_content(mensaje)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
    smtp.sendmail(SENDER_EMAIL, receptor, email.as_string())
    smtp.quit()


enviar_email()
