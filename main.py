import streamlit as st
import PyPDF2
import google.generativeai as genai
genai.__version__
from google.colab import userdata
genai.configure(api_key=userdata.get('GeminiKey'))


@def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        st.info("Cargando archivo")
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        extracted_text = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text
        return extracted_text

@def list_files():
    for file in genai.list_files():
        nombre_archivos += file.display_name
    return nombre_archivos
@def delete_file(file_name):
    genai.delete_file(document_file.file_name)
    estado = "Eliminacion exitosa"
    return estado

    
st.title("Sistema de Gestión del Conocimiento")
st.logo("sgc.png")

ROLES = [None,"Consulta", "Carga", "Admin"]
opcion = st.selectbox("Selecciona un rol: ", ROLES)

if opcion == "Consulta":
    st.write("Ingresó a consulta con IA")
    model = genai.GenerativeModel(model_name = "gemini-1.5-flash")
    pregunta = st.text_input("Ingresa tu pregunta")
    response = model.generate_content([pregunta, archivo])
    st.write(response.text)
    #prompt =Texto de entrada 
if opcion == "Carga":
    st.write("Ingresó a la carga de archivos")
    carga_archivo = st.file_uploader("Sube un archivo PDF", type = ["pdf","txt"],accept_multiples = True)
    carga_texto = extract_text_from_pdf(carga_archivo)
    st.write("Archivos cargados exitosamente")
    #Subida de archivos en local
if opcion == "Admin":
    st.write("Ingresó al dashboard del sistema")
#role = st.session_state.role


