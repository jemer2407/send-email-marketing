import streamlit as st
import pandas as pd
import uuid
from datetime import datetime
from google_sheets import GoogleSheet # type: ignore


def hoy():

	hoy=datetime.today()
	return str(hoy)

def generate_uid():
    return str(uuid.uuid4())

# VARIABLES
# ---- credenciales, nombre del documento de hoja de calculo y nombre de la hoja ----
credentials = st.secrets["google"]["credentials_google"]
document_name = "bbdd-citas-masajes"
sheet_name = "contactos"
# ---------------------------------


# FIN VARIABLES ------------------

# INICIO FRONT-END

st.title("Contactos")

with st.spinner("Cargando datos...."):

    # crear objeto google sheets
    google = GoogleSheet(credentials,document_name,sheet_name)
    contactos = google.get_all_values()
    df = pd.DataFrame(contactos)
    data_frame = st.dataframe(df,use_container_width=True,column_order=("nombre","email","fecha-nacimiento"),hide_index=True)

#nuevo_usuario = st.button("Nuevo usuario")

#if nuevo_usuario:

with st.form(key="my_form"):
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    
    nuevo_usuario = st.form_submit_button(label="Añadir contacto")

    if nuevo_usuario:
        if nombre and email:
            with st.spinner("Añadiendo nuevo contacto...."):
                uid = generate_uid()
                google.write_data(google.get_last_row_range(),[[uid,nombre,email,None,hoy()]])                
                
                # ---------- actualizar dataframe añadiendo al nuevo contacto ---------------
                contacto = [{'uid':uid,'nombre':nombre,'email':email,'fecha-nacimiento':"",'timestamp':hoy()}]
                df_nuevo = pd.DataFrame(contacto)
                data_frame.add_rows(df_nuevo)
                # ------------------------------------------------
                st.success("Usuario añadido con éxito")
            
        else:
            st.error("Por favor, rellene todos los campos")





