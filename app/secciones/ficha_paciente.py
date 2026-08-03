"""
Seccion: Ficha Paciente.

Replica del formulario "Ficha clinica del paciente" de la plantilla
HTML de referencia. Bloque 1: Datos personales.
"""

from datetime import date

import streamlit as st

from utils.estado import get_paciente, actualizar_paciente
from utils.validaciones import validar_rut


def mostrar():
    paciente = get_paciente()

    st.markdown("#### 🥗 Ficha clínica del paciente")

    col1, col2, col3 = st.columns(3)

    with col2:
        fecha_nacimiento = st.date_input(
            "Fecha de nacimiento",
            value=paciente.get("fecha_nacimiento") or date(2000, 1, 1),
            min_value=date(1920, 1, 1),
            max_value=date.today(),
            key="fp_fecha_nacimiento",
        )

        opciones_sexo = ["", "Femenino", "Masculino"]
        sexo_actual = paciente.get("sexo") or ""
        sexo = st.selectbox(
            "Sexo",
            options=opciones_sexo,
            index=opciones_sexo.index(sexo_actual) if sexo_actual in opciones_sexo else 0,
            key="fp_sexo",
        )
        correo = st.text_input(
            "Correo electrónico", value=paciente.get("correo") or "", key="fp_correo"
        )
        ocupacion = st.text_input(
            "Ocupación", value=paciente.get("ocupacion") or "", key="fp_ocupacion"
        )

    hoy = date.today()
    edad = (
        hoy.year
        - fecha_nacimiento.year
        - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    )

    with col1:
        nombre = st.text_input(
            "Apellidos y nombres", value=paciente.get("nombre") or "", key="fp_nombre"
        )
        st.text_input("Edad (años)", value=f"{edad}", disabled=True, key=f"fp_edad_{fecha_nacimiento.isoformat()}")        
        telefono = st.text_input(
            "Teléfono", value=paciente.get("telefono") or "", key="fp_telefono"
        )
        ciudad = st.text_input(
            "Ciudad", value=paciente.get("ciudad") or "", key="fp_ciudad"
        )
        prevision = st.text_input(
            "Previsión / Seguro", value=paciente.get("prevision") or "", key="fp_prevision"
        )

    with col3:
        rut = st.text_input(
            "RUT", value=paciente.get("rut") or "", key="fp_rut",
            placeholder="12.345.678-9",
        )
        if rut and not validar_rut(rut):
            st.caption("⚠️ RUT invalido")
        fecha_consulta = st.date_input(
            "Fecha de consulta",
            value=paciente.get("fecha_consulta") or date.today(),
            key="fp_fecha_consulta",
        )
        direccion = st.text_input(
            "Dirección", value=paciente.get("direccion") or "", key="fp_direccion"
        )
        opciones_actividad = ["Sedentario", "Ligero", "Moderado", "Intenso", "Muy intenso"]
        actividad_actual = paciente.get("nivel_actividad") or "Sedentario"
        nivel_actividad = st.selectbox(
            "Nivel de actividad física",
            options=opciones_actividad,
            index=opciones_actividad.index(actividad_actual) if actividad_actual in opciones_actividad else 0,
            key="fp_nivel_actividad",
        )


    st.markdown("#### Antecedentes médicos y familiares")

    motivo_consulta = st.text_area(
        "Motivo de consulta",
        value=paciente.get("motivo_consulta") or "",
        height=90,
        key="fp_motivo_consulta",
    )

    col4, col5 = st.columns(2)

    with col4:
        con_quien_vive = st.text_area(
            "Con quién vive",
            value=paciente.get("con_quien_vive") or "",
            height=90,
            key="fp_con_quien_vive",
        )
        deposicion = st.text_input(
            "¿Cómo son sus deposiciones?", value=paciente.get("deposicion") or "", key="fp_deposicion"
        )
        patologias = st.text_area(
            "Patologías actuales",
            value=paciente.get("patologias") or "",
            height=90,
            key="fp_patologias",
        )
        cirugias = st.text_area(
            "Cirugías / hospitalizaciones previas",
            value=paciente.get("cirugias") or "",
            height=90,
            key="fp_cirugias",
        )


    with col5:
        antecedentes_familiares = st.text_area(
            "Antecedentes familiares relevantes",
            value=paciente.get("antecedentes_familiares") or "",
            height=90,
            key="fp_antecedentes_familiares",
        )
        orina = st.text_input(
            "Color de orina", value=paciente.get("orina") or "", key="fp_orina"
        )
        alergias = st.text_area(
            "Alergias / intolerancias alimentarias",
            value=paciente.get("alergias") or "",
            height=90,
            key="fp_alergias",
        )
        medicamentos = st.text_area(
            "Medicamentos actuales",
            value=paciente.get("medicamentos") or "",
            height=90,
            key="fp_medicamentos",
        )
        

    st.markdown("#### Hábitos alimentarios y estilo de vida")

    col6, col7, col8 = st.columns(3)

    with col6:
        n_comidas = st.text_input(
            "N° de comidas al día",
            value=paciente.get("n_comidas") or "",
            key="fp_n_comidas",
        )
        alimentos_preferidos = st.text_input(
            "Alimentos preferidos",
            value=paciente.get("alimentos_preferidos") or "",
            key="fp_alimentos_preferidos",
        )
        tabaquismo = st.text_input(
            "Tabaquismo",
            value=paciente.get("tabaquismo") or "",
            key="fp_tabaquismo",
        )

    with col7:
        horario_comidas = st.text_input(
            "Horario de comidas habitual",
            value=paciente.get("horario_comidas") or "",
            key="fp_horario_comidas",
        )
        alimentos_rechaza = st.text_input(
            "Alimentos que rechaza / evita",
            value=paciente.get("alimentos_rechaza") or "",
            key="fp_alimentos_rechaza",
        )
        horas_sueno = st.text_input(
            "Horas de sueño promedio",
            value=paciente.get("horas_sueno") or "",
            key="fp_horas_sueno",
        )

    with col8:
        consumo_agua = st.text_input(
            "Consumo de agua al día (L)",
            value=paciente.get("consumo_agua") or "",
            key="fp_consumo_agua",
        )
        consumo_alcohol = st.text_input(
            "Consumo de alcohol (frecuencia)",
            value=paciente.get("consumo_alcohol") or "",
            key="fp_consumo_alcohol",
        )
        suplementos = st.text_input(
            "Suplementos actuales",
            value=paciente.get("suplementos") or "",
            key="fp_suplementos",
        )

    actividad_fisica = st.text_area(
        "Actividad física (descripción)",
        value=paciente.get("actividad_fisica") or "",
        height=90,
        key="fp_actividad_fisica",
    )

    objetivo = st.text_area(
        "Objetivo del paciente",
        value=paciente.get("objetivo") or "",
        height=90,
        key="fp_objetivo",
    )

    actualizar_paciente(
        nombre=nombre,
        rut=rut,
        fecha_nacimiento=fecha_nacimiento,
        sexo=sexo,
        fecha_consulta=fecha_consulta,
        edad=edad,
        telefono=telefono,
        correo=correo,
        direccion=direccion,
        ciudad=ciudad,
        ocupacion=ocupacion,
        nivel_actividad=nivel_actividad,
        prevision=prevision,
        patologias=patologias,
        alergias=alergias,
        medicamentos=medicamentos,
        antecedentes_familiares=antecedentes_familiares,
        cirugias=cirugias,
        n_comidas=n_comidas,
        horario_comidas=horario_comidas,
        consumo_agua=consumo_agua,
        alimentos_preferidos=alimentos_preferidos,
        alimentos_rechaza=alimentos_rechaza,
        consumo_alcohol=consumo_alcohol,
        tabaquismo=tabaquismo,
        horas_sueno=horas_sueno,
        suplementos=suplementos,
        actividad_fisica=actividad_fisica,
        objetivo=objetivo,
        motivo_consulta=motivo_consulta,
        con_quien_vive=con_quien_vive,
        deposicion=deposicion,
        orina=orina,
    )

    if nombre:
        st.success(f"Datos de {nombre} guardados.")