# Ej29 · tienda.py · Versión 1.0, la que ya está "en producción"

PRECIOS = {"cuaderno": 2.5, "boli": 0.8, "mochila": 25}
IVA = 0.21

# ADAPTATIVO (PASO 4): sustituye IVA por un diccionario de impuestos por región:
#   IMPUESTOS = {"peninsula": ("IVA", 0.21), "canarias": ("IGIC", 0.07)}
# y añade un parámetro region="peninsula" a mostrar_ticket.

# EVOLUTIVO (PASO 3): crea un diccionario de cupones:  CUPONES = {"ED10": 0.10}
# y añade un parámetro cupon=None a mostrar_ticket. Si hay cupón, resta el descuento
# al subtotal ANTES de calcular el impuesto, y muestra la línea "Descuento ED10: -3.90".


def mostrar_ticket(pedido):
    t = 0
    for p, c in pedido:
        print(p, c, PRECIOS[p], PRECIOS[p] * c)
        # CORRECTIVO (PASO 1): esta línea tiene un fallo. Pista: ¿se está ACUMULANDO?
        t = PRECIOS[p] * c
    # PERFECTIVO (PASO 2): el código y el ticket son poco claros.
    #  - Cambia los nombres t, p, c por subtotal, producto, cantidad.
    #  - Alinea las columnas y usa 2 decimales. Por ejemplo, para cada línea:
    #      print(f"{producto:<10}{cantidad:>3} x {precio:>5.2f} = {importe:>6.2f}")
    #    y para los totales:  print(f"{'Subtotal:':<24}{subtotal:>7.2f}")
    print("Subtotal", t)
    print("IVA", t * IVA)
    print("TOTAL", t + t * IVA)


pedido = [("cuaderno", 4), ("boli", 5), ("mochila", 1)]
print("--- Pedido en la península ---")
mostrar_ticket(pedido)
# EVOLUTIVO: añade aquí el mismo pedido con el cupón ED10.
# ADAPTATIVO: añade aquí el mismo pedido en Canarias.
