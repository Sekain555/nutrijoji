"""
Manejo del estado compartido de la sesión (session_state).

Toda la información del paciente vive en un solo diccionario dentro de
st.session_state para que las distintas páginas/pestañas puedan leerla
y escribirla sin perder datos al navegar.
"""

import streamlit as st


CAMPOS_FICHA_PACIENTE = {
    "nombre": "",
    "sexo": "",
    "fecha_nacimiento": None,
    "edad": None,
    "correo": "",
    "fecha_consulta": None,
    "diagnostico": "",
}


def inicializar_estado():
    """Crea las claves necesarias en session_state si todavía no existen."""
    if "paciente" not in st.session_state:
        st.session_state["paciente"] = dict(CAMPOS_FICHA_PACIENTE)


def get_paciente() -> dict:
    inicializar_estado()
    return st.session_state["paciente"]


def actualizar_paciente(**kwargs):
    inicializar_estado()
    st.session_state["paciente"].update(kwargs)
