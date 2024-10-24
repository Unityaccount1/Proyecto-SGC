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

logout_page = st.Page(logout, title="Cerrar sesión", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
consulta = st.Page(
    consulta,
    title = "Consulta",
    icon = ":material/handyman:",
)
request_pages = [consulta]

st.title("Sistema de Gestión del Conocimiento")
st.logo("sgc.png")

page_dict = {}
if st.session_state.role in ["Consulta"]:
    page_dict["Prueba"] = request_pages
else:
    pg = st.navigation([st.Page(login)])
    pg.run()
