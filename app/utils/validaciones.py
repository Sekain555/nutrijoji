"""
Funciones de validacion.
"""


def validar_rut(rut: str) -> bool:
    """
    Valida un RUT chileno con su digito verificador.
    Acepta formatos como '12345678-9' o '12.345.678-9'.
    Retorna True si el formato y el digito verificador son correctos.
    """
    if not rut:
        return False

    rut_limpio = rut.replace(".", "").replace("-", "").strip().upper()

    if len(rut_limpio) < 2:
        return False

    cuerpo = rut_limpio[:-1]
    dv_ingresado = rut_limpio[-1]

    if not cuerpo.isdigit():
        return False

    suma = 0
    multiplicador = 2
    for digito in reversed(cuerpo):
        suma += int(digito) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    resto = suma % 11
    dv_calculado = 11 - resto
    if dv_calculado == 11:
        dv_esperado = "0"
    elif dv_calculado == 10:
        dv_esperado = "K"
    else:
        dv_esperado = str(dv_calculado)

    return dv_ingresado == dv_esperado