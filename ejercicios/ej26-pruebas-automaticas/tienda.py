# Ej26 · tienda.py · Funciones de una tienda en línea

TIPOS_IVA = {"general": 0.21, "reducido": 0.10, "superreducido": 0.04}


def precio_con_iva(precio, tipo="general"):
    """Devuelve el precio con el IVA del tipo indicado, redondeado a 2 decimales."""
    return round(precio * (1 + TIPOS_IVA[tipo]), 2)


def aplicar_descuento(precio, porcentaje):
    """Devuelve el precio después de restarle el porcentaje, redondeado a 2 decimales."""
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return round(precio * porcentaje / 100, 2)
