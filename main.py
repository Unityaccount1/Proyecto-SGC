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
'''
request_1 = st.Page(
    "request/request_1.py",
    title="Request 1",
    icon=":material/help:",
    default=(role == "Requester"),
)
request_2 = st.Page(
    "request/request_2.py", title="Request 2", icon=":material/bug_report:"
)
respond_1 = st.Page(
    "respond/respond_1.py",
    title="Respond 1",
    icon=":material/healing:",
    default=(role == "Responder"),
)
respond_2 = st.Page(
    "respond/respond_2.py", title="Respond 2", icon=":material/handyman:"
)
admin_1 = st.Page(
    "admin/admin_1.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)
admin_2 = st.Page("admin/admin_2.py", title="Admin 2", icon=":material/security:")
'''
consulta = st.Page(
    "/consulta.py",
    tittle = "Consulta",
    icon = ":material/person_add:",
    default = (role == "Admin"),
)
request_pages = [consulta]

st.title("Gestor de peticiones")
st.logo("/sgc.png")

page_dict = {}
if st.session_state.role in ["Consulta"]:
    page_dict["Consulta"] = request_pages
else:
    pg = st.navigation([st.Page(login)])

pg.run()
