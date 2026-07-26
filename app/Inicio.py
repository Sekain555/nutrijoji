"""
Punto de entrada de la app Streamlit.

Se usa el sistema de multipágina nativo de Streamlit (carpeta /pages).
Cada pantalla de evaluación (Ficha Paciente, y las que se definan con
Josefa más adelante) vive como un archivo separado en app/pages/.
"""

import streamlit as st

from utils.estilos import aplicar_estilos, encabezado
from utils.estado import inicializar_estado, get_paciente

st.set_page_config(
    page_title="Evaluación Alimentaria",
    page_icon="🥗",
    layout="wide",
)

aplicar_estilos()
inicializar_estado()

encabezado(
    "🥗 Calculadora de Evaluación Alimentaria",
    "Completa las secciones desde el menú lateral. Los datos se guardan "
    "automáticamente mientras navegas entre pantallas.",
)

paciente = get_paciente()

st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
st.subheader("Estado actual")
if paciente.get("nombre"):
    st.write(f"Paciente en curso: **{paciente['nombre']}**")
else:
    st.write(
        "Todavía no hay datos ingresados. Empieza por la sección "
        "**Ficha Paciente** en el menú lateral."
    )
st.markdown("</div>", unsafe_allow_html=True)
