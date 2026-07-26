"""
Manejo del estado compartido de la sesion (session_state).

Toda la informacion del paciente vive en un solo diccionario dentro de
st.session_state para que las distintas pestanas puedan leerla y
escribirla sin perder datos al navegar.

Ademas se define el ORDEN de las secciones y sus campos "requeridos"
para poder mostrar advertencias (no bloqueos) cuando el usuario entra
a una pestana sin haber completado la anterior.
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

ORDEN_SECCIONES = [
    {
        "id": "ficha_paciente",
        "titulo": "Ficha paciente",
        "campos_requeridos": ["paciente.nombre", "paciente.sexo"],
    },
    {
        "id": "antropometria",
        "titulo": "Antropometria",
        "campos_requeridos": [],
    },
    {
        "id": "calculo_energetico",
        "titulo": "Calculo energetico",
        "campos_requeridos": [],
    },
    {
        "id": "plan_alimentario",
        "titulo": "Plan alimentario",
        "campos_requeridos": [],
    },
    {
        "id": "recordatorio_24h",
        "titulo": "Recordatorio 24h",
        "campos_requeridos": [],
    },
    {
        "id": "seguimiento",
        "titulo": "Seguimiento",
        "campos_requeridos": [],
    },
    {
        "id": "bioquimicos",
        "titulo": "Indicadores bioquimicos",
        "campos_requeridos": [],
    },
    {
        "id": "hidratacion",
        "titulo": "Hidratacion",
        "campos_requeridos": [],
    },
    {
        "id": "gestante",
        "titulo": "Gestante",
        "campos_requeridos": [],
    },
    {
        "id": "resumen",
        "titulo": "Resumen ejecutivo",
        "campos_requeridos": [],
    },
]


def inicializar_estado():
    if "paciente" not in st.session_state:
        st.session_state["paciente"] = dict(CAMPOS_FICHA_PACIENTE)


def get_paciente() -> dict:
    inicializar_estado()
    return st.session_state["paciente"]


def actualizar_paciente(**kwargs):
    inicializar_estado()
    st.session_state["paciente"].update(kwargs)


def _leer_campo(ruta: str):
    partes = ruta.split(".")
    valor = st.session_state
    for parte in partes:
        if isinstance(valor, dict) and parte in valor:
            valor = valor[parte]
        else:
            return None
    return valor


def seccion_completa(id_seccion: str) -> bool:
    inicializar_estado()
    definicion = next((s for s in ORDEN_SECCIONES if s["id"] == id_seccion), None)
    if definicion is None:
        return True
    for ruta in definicion["campos_requeridos"]:
        if not _leer_campo(ruta):
            return False
    return True


def secciones_previas_incompletas(id_seccion: str) -> list:
    incompletas = []
    for seccion in ORDEN_SECCIONES:
        if seccion["id"] == id_seccion:
            break
        if not seccion_completa(seccion["id"]):
            incompletas.append(seccion["titulo"])
    return incompletas