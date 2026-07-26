"""
Estilos visuales compartidos.

Streamlit no permite reproducir 1:1 un HTML/CSS a medida, pero podemos
inyectar CSS para acercarnos a la paleta rosa/morado y tipografía
(Quicksand + Nunito Sans) de la plantilla de referencia que le gustó
a la clienta.
"""

import streamlit as st

CSS_BASE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&family=Nunito+Sans:wght@400;600;700;800&display=swap');

:root {
    --pink-soft: #f8d6e8;
    --pink-mid: #f2a9cf;
    --purple-soft: #e3d3f5;
    --purple-mid: #c497e0;
    --purple-deep: #9a5fbf;
    --ink: #4a3358;
    --ink-soft: #8a7594;
}

html, body, [class*="css"] {
    font-family: 'Nunito Sans', sans-serif;
    color: var(--ink);
}

h1, h2, h3 {
    font-family: 'Quicksand', sans-serif !important;
    color: var(--purple-deep) !important;
}

/* Encabezado tipo "hero" con degradado rosa-morado */
.encabezado-app {
    background: linear-gradient(120deg, var(--pink-mid), var(--purple-mid));
    padding: 22px 28px;
    border-radius: 18px;
    color: #ffffff;
    margin-bottom: 22px;
}
.encabezado-app h1 {
    color: #ffffff !important;
    margin: 0;
    font-size: 26px;
}
.encabezado-app p {
    margin: 6px 0 0;
    opacity: 0.92;
    font-size: 14px;
}

/* Tarjetas de contenido */
.tarjeta {
    background: #ffffff;
    border-radius: 18px;
    padding: 20px 22px;
    box-shadow: 0 6px 20px rgba(154, 95, 191, .12);
    margin-bottom: 18px;
}

/* Botones primarios */
div.stButton > button {
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    border-radius: 10px;
    border: none;
    background: linear-gradient(120deg, var(--pink-mid), var(--purple-mid));
    color: #ffffff;
}
div.stButton > button:hover {
    filter: brightness(1.06);
}
</style>
"""


def aplicar_estilos():
    st.markdown(CSS_BASE, unsafe_allow_html=True)


def encabezado(titulo: str, subtitulo: str = ""):
    st.markdown(
        f"""
        <div class="encabezado-app">
            <h1>{titulo}</h1>
            <p>{subtitulo}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
