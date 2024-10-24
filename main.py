import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Consulta", "Carga", "Admin"]


def login():

    st.header("Inicio de sesión")
    role = st.selectbox("Escoge tu rol: ", ROLES)

    if st.button("Ingresar"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()
def consulta():
    st.write("Bienvenido a la seccion de consulta")
    

role = st.session_state.role

st.title("Sistema de Gestión del Conocimiento")
st.logo("sgc.png")

opcion = st.selectbox("Selecciona un rol: ", ROLES)

if opcion == "Consulta":
    st.write("Bienvenido a consulta")
if opcion == "Carga":
    st.write("Bienvenido a la carga de archivos")
if opcion == "Admin":
    st.write("Bienvenido a la zona administrativa")
else:
    logout()
