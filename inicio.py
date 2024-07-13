import streamlit as st
from google_auth_st import add_auth

page_title = "Inicio"
page_icon = ":house:"
layout="wide"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.title("Primera página")
