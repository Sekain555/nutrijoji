"""
Punto de entrada de la app Streamlit.

Navegacion por pestanas (st.tabs), todo en una sola pagina. El orden
de las pestanas sigue ORDEN_SECCIONES en utils/estado.py. Si el
usuario entra a una pestana sin haber completado una anterior, se
muestra una advertencia (no bloqueante) pero se le deja seguir.
"""

import streamlit as st

from utils.estilos import aplicar_estilos, encabezado
from utils.estado import inicializar_estado, ORDEN_SECCIONES, secciones_previas_incompletas
from secciones import (
    ficha_paciente,
    antropometria,
    calculo_energetico,
    plan_alimentario,
    recordatorio_24h,
    seguimiento,
    bioquimicos,
    hidratacion,
    gestante,
    resumen,
)

st.set_page_config(
    page_title="Evaluacion Alimentaria",
    page_icon="🥗",
    layout="wide",
)

aplicar_estilos()
inicializar_estado()

encabezado(
    "🥗 Calculadora de Evaluacion Alimentaria",
    "Navega libremente entre pestanas. Si falta informacion de un paso "
    "anterior, veras una advertencia, pero puedes seguir avanzando.",
)

RENDERERS = {
    "ficha_paciente": ficha_paciente.mostrar,
    "antropometria": antropometria.mostrar,
    "calculo_energetico": calculo_energetico.mostrar,
    "plan_alimentario": plan_alimentario.mostrar,
    "recordatorio_24h": recordatorio_24h.mostrar,
    "seguimiento": seguimiento.mostrar,
    "bioquimicos": bioquimicos.mostrar,
    "hidratacion": hidratacion.mostrar,
    "gestante": gestante.mostrar,
    "resumen": resumen.mostrar,
}

titulos = [seccion["titulo"] for seccion in ORDEN_SECCIONES]
tabs = st.tabs(titulos)

for tab, seccion in zip(tabs, ORDEN_SECCIONES):
    with tab:
        faltantes = secciones_previas_incompletas(seccion["id"])
        if faltantes:
            st.warning(
                "Faltan datos en: " + ", ".join(faltantes) + ". "
                "Puedes completarlos ahora o seguir de todas formas."
            )

        st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
        RENDERERS[seccion["id"]]()
        st.markdown("</div>", unsafe_allow_html=True)