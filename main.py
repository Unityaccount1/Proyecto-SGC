import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Consulta", "Carga", "Admin"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Cerrar sesión", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
consulta = st.Page(
    "consulta.py",
    title = "Consulta",
    icon = ":material/person_add:",
    default = (role == "Consulta"),
)
request_pages = [consulta]

st.title("Gestor de peticiones")
st.logo("sgc.png")

page_dict = {}
if st.session_state.role in ["Consulta"]:
    page_dict["Consulta"] = request_pages
else:
    pg = st.navigation([st.Page(login)])
    pg.run()
