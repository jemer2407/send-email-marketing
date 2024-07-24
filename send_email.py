import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

def send_email(email, subject, message):

    # credenciales
    user = st.secrets["emails"]["smtp_user"]
    password = st.secrets["emails"]["smtp_password"]

    sender_email = "Salon de Masajes Cordoba"

    # configuracion del servidor
    msg = MIMEMultipart()

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # parametros del mensaje
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject

    
    msg.attach(MIMEText(message,'plain'))

    # Conexión al servidor
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)   # configuracion servidor
        server.starttls()   # inicializamos el servidor
        server.login(user,password) # nos logueamos
        server.sendmail(sender_email, email, msg.as_string())   # envio de correo
        server.quit()   # cerramos la conexion con el servidor
    except smtplib.SMTPException as e:
        st.error("Error al enviar el email")



