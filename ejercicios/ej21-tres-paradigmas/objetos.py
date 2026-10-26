# Ej21 · Paradigma ORIENTADO A OBJETOS: objetos con datos (atributos) y comportamiento (métodos)


# PASO 1: crea la clase Producto con un constructor que guarde nombre y precio:
#     class Producto:
#         def __init__(self, nombre, precio):
#             self.nombre = nombre
#             self.precio = precio
#
#         def precio_final(self):
#             ...  # 10 % de descuento si el precio es mayor que 20


# PASO 2: crea la clase Carrito con:
#   - __init__: crea self.productos como lista vacía
#   - añadir(self, producto): añade el producto a la lista
#   - total(self): devuelve la suma del precio_final() de todos sus productos


# PASO 3: crea un carrito, añade estos productos y muestra el total:
#   Libro 12.5, Zapatillas 30, Cuaderno 8, Auriculares 45, Mochila 22
#   print(f"Total a pagar: {carrito.total():.2f} €")

