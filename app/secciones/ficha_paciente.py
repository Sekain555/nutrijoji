"""
Seccion: Ficha Paciente.

Replica funcional (en Streamlit) de la seccion "Antecedentes del
paciente" de la plantilla HTML de referencia. Se expone como una
funcion `mostrar()` para insertarse dentro de una pestana de st.tabs().
"""

from datetime import date

import streamlit as st

from utils.estado import get_paciente, actualizar_paciente


def mostrar():
    paciente = get_paciente()

    col1, col2 = st.columns(2)

    with col1:
        nombre = st.text_input(
            "Nombre y apellido", value=paciente.get("nombre") or "", key="fp_nombre"
        )
        opciones_sexo = ["", "Femenino", "Masculino"]
        sexo_actual = paciente.get("sexo") or ""
        sexo = st.selectbox(
            "Sexo",
            options=opciones_sexo,
            index=opciones_sexo.index(sexo_actual) if sexo_actual in opciones_sexo else 0,
            key="fp_sexo",
        )
        fecha_nacimiento = st.date_input(
            "Fecha de nacimiento",
            value=paciente.get("fecha_nacimiento") or date(2000, 1, 1),
            min_value=date(1920, 1, 1),
            max_value=date.today(),
            key="fp_fecha_nacimiento",
        )

    with col2:
        correo = st.text_input(
            "Correo electronico", value=paciente.get("correo") or "", key="fp_correo"
        )
        fecha_consulta = st.date_input(
            "Fecha de consulta",
            value=paciente.get("fecha_consulta") or date.today(),
            key="fp_fecha_consulta",
        )

    hoy = date.today()
    edad = (
        hoy.year
        - fecha_nacimiento.year
        - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    )
    st.metric("Edad (calculada)", f"{edad} anos")

    diagnostico = st.text_area(
        "Diagnostico / observaciones generales",
        value=paciente.get("diagnostico") or "",
        height=100,
        key="fp_diagnostico",
    )

    actualizar_paciente(
        nombre=nombre,
        sexo=sexo,
        fecha_nacimiento=fecha_nacimiento,
        edad=edad,
        correo=correo,
        fecha_consulta=fecha_consulta,
        diagnostico=diagnostico,
    )

    if nombre:
        st.success(f"Datos de {nombre} guardados.")