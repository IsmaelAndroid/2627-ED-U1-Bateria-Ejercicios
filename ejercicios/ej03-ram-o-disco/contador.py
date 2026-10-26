# Ej03 · RAM o disco: ¿qué sobrevive?
import os

FICHERO = "visitas.txt"

# PASO 1: crea una variable contador_ram con valor 0 y súmale 1.
# Esta variable vive en la RAM mientras el programa se ejecuta.


# PASO 2: lee el contador guardado en disco.
# Si el fichero existe (os.path.exists(FICHERO)), ábrelo, lee su contenido
# y conviértelo a número con int(). Si no existe, el contador empieza en 0.
# Guarda el resultado en la variable contador_disco.


# PASO 3: súmale 1 a contador_disco y escribe el nuevo valor en el fichero.
# Pista:
#     with open(FICHERO, "w") as f:
#         f.write(str(contador_disco))


# PASO 4: muestra los dos contadores con este formato:
#   Contador en RAM (variable): 1
#   Contador en disco (fichero): 3

