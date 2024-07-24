import streamlit as st
import time as t
from send_email import send_email # type: ignore
from google_sheets import GoogleSheet # type: ignore

# VARIABLES
# ---- credenciales, nombre del documento de hoja de calculo y nombre de la hoja ----
credentials = st.secrets["google"]["credentials_google"]
document_name = "bbdd-citas-masajes"
sheet_name = "contactos"
contador = 0

# ------- variable de sesion --------

if "first_time" not in st.session_state:
    st.session_state.first_time = True
# ---------------------------------

st.title("Nueva campaña de email marketing")

st.header("Crear nueva Campaña")

subject = st.text_input("Asunto")
message = st.text_area("Mensaje")

lista_contactos = st.selectbox("Selecciona la lista de contactos",["Principal"])

submit = st.checkbox("He revisado el mensaje y deseo enviarlo a los contactos seleccionados")
enviar = st.button("Enviar email")

if enviar:
    if subject and message and submit:
        with st.spinner("Enviando campaña...."):
            google = GoogleSheet(credentials,document_name,sheet_name)
            contactos = google.get_all_values()
        
            for contacto in contactos:
                send_email(contacto["email"],subject,message)
                contador += 1
                t.sleep(10)

        st.success("Campaña enviada correctamente")
        st.write(f"Se ha enviado el email a {contador} contactos")
    else:
        st.warning("Por favor, rellene todos los campos y marque la casilla de confirmación")



