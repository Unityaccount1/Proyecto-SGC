import streamlit as st


st.title("Sistema de Gestión del Conocimiento")
st.logo("sgc.png")

ROLES = [None,"Consulta", "Carga", "Admin"]
opcion = st.selectbox("Selecciona un rol: ", ROLES)
if opcion == "Consulta":
    st.write("Ingresó a consulta con IA")
if opcion == "Carga":
    st.write("Ingresó a la carga de archivos")
if opcion == "Admin":
    st.write("Ingresó al dashboard del sistema")
#role = st.session_state.role


