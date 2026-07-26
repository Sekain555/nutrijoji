# Calculadora de Evaluación Alimentaria

Proyecto en Python + Streamlit para generar un resumen de evaluación
alimentario, basado en la plantilla de referencia y los criterios
usados por la nutricionista.

## Estructura

```
app/
  Inicio.py              # Punto de entrada (página principal)
  pages/
    1_Ficha_Paciente.py   # Antecedentes generales del paciente
  utils/
    estado.py             # Manejo del estado compartido (session_state)
    estilos.py             # CSS y componentes visuales (paleta rosa/morado)
  data/                    # Acá irán las tablas de referencia (porciones, rangos, etc.)
requirements.txt
```

## Cómo correrlo localmente

```bash
pip install -r requirements.txt
cd app
streamlit run Inicio.py
```

## Próximos pasos

- Definir con Josefa las categorías/pantallas exactas que ella evalúa
  (además de Ficha Paciente) para agregar el resto de páginas en
  `app/pages/`.
- Cargar en `app/data/` las tablas de porciones, rangos y criterios de
  los archivos de referencia, a medida que se vayan necesitando.
- Implementar exportación a PDF del resumen final.
- Implementar envío por correo (al final del desarrollo, una vez
  definido el hosting/dominio).
