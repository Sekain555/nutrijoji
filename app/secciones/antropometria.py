"""
Seccion: Evaluacion antropometrica.

Replica de la seccion "Evaluacion antropometrica" de la plantilla
HTML de referencia: parametros medidos (como campos individuales) +
bloque de indices y clasificaciones (calculo automatico, pendiente de
formulas).
"""

import streamlit as st

from utils.estado import get_paciente, actualizar_paciente


PARAMETROS = [
    ("peso", "Peso corporal", "kg"),
    ("talla", "Talla (Estatura)", "cm"),
    ("circ_cintura", "Circunferencia de cintura", "cm"),
    ("circ_cadera", "Circunferencia de cadera", "cm"),
    ("circ_brazo", "Circunferencia de brazo", "cm"),
    ("pliegue_tricipital", "Pliegue tricipital", "mm"),
    ("pliegue_subescapular", "Pliegue subescapular", "mm"),
    ("pliegue_suprailiaco", "Pliegue suprailíaco", "mm"),
    ("pliegue_abdominal", "Pliegue abdominal", "mm"),
    ("masa_muscular", "Masa muscular (bioimpedancia)", "kg"),
    ("masa_grasa", "Masa grasa (bioimpedancia)", "kg"),
    ("pct_graso", "Porcentaje graso (bioimpedancia)", "%"),
    ("agua_corporal", "Agua corporal total", "%"),
    ("masa_osea", "Masa ósea", "kg"),
]


def mostrar():
    paciente = get_paciente()

    st.markdown("#### 📏 Evaluación antropométrica")

    valores = {}

    col_param, col_valor, col_unidad, col_anterior, col_diferencia = st.columns([2.5, 1.5, 1, 1.5, 1.1])
    with col_param:
        st.markdown("**Parámetro**")
    with col_valor:
        st.markdown("**Valor ingresado**")
    with col_unidad:
        st.markdown("**Unidad**")
    with col_anterior:
        st.markdown("**Valor anterior**")
    with col_diferencia:
        st.markdown("**Diferencia**")

    st.divider()

    for id_param, etiqueta, unidad in PARAMETROS:
        col_param, col_valor, col_unidad, col_anterior, col_diferencia = st.columns([2.3, 1.4, 0.8, 1.4, 1.1])

        with col_param:
            st.markdown(f"{etiqueta}")
        with col_valor:
            valor_ingresado = st.number_input(
                "Valor ingresado",
                value=paciente.get(f"{id_param}_ingresado") or 0.0,
                key=f"antro_{id_param}_ingresado",
                label_visibility="collapsed",
            )
        with col_unidad:
            st.markdown(unidad)
        with col_anterior:
            st.markdown("*Sin datos previos*")
        with col_diferencia:
            st.markdown("*-*")

        valores[f"{id_param}_ingresado"] = valor_ingresado

    st.markdown("##### Índices y clasificaciones (cálculo automático)")
    st.caption(
        "Pendiente: se completará cuando se definan las fórmulas y rangos "
        "de referencia."
    )

    colA, colB, colC = st.columns(3)

    with colA:
        st.text_input("IMC (kg/m²)", value="", disabled=True, key="antro_imc")
        st.text_input("% Adecuación de peso", value="", disabled=True, key="antro_adecuacion")
        st.text_input("Riesgo ICC", value="", disabled=True, key="antro_riesgo_icc")
        st.text_input("% Masa grasa (bioimpedancia)", value="", disabled=True, key="antro_pct_grasa")

    with colB:
        st.text_input("Clasificación IMC (OMS)", value="", disabled=True, key="antro_clasificacion_imc")
        st.text_input("Clasificación % adecuación", value="", disabled=True, key="antro_clasificacion_adecuacion")
        st.text_input("ICT — cintura/talla", value="", disabled=True, key="antro_ict")
        st.text_input("Clasificación % grasa", value="", disabled=True, key="antro_clasificacion_grasa")

    with colC:
        st.text_input("Peso ideal — Lorentz (kg)", value="", disabled=True, key="antro_peso_ideal")
        st.text_input("ICC — cintura/cadera", value="", disabled=True, key="antro_icc")
        st.text_input("Suma de 4 pliegues (mm)", value="", disabled=True, key="antro_suma_pliegues")
        st.text_input("Masa libre de grasa (kg)", value="", disabled=True, key="antro_masa_libre_grasa")

    st.info(
        "Referencia IMC (OMS): <16.0 Desnutrición severa · <17.0 Desnutrición "
        "moderada · <18.5 Desnutrición leve · 18.5–24.9 Peso normal · "
        "25.0–29.9 Sobrepeso · 30.0–34.9 Obesidad grado I · 35.0–39.9 "
        "Obesidad grado II · ≥40.0 Obesidad grado III"
    )

    actualizar_paciente(**valores)