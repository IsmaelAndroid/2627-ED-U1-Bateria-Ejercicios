# Ej02 · Clasifica el software
# Completa el código debajo de cada PASO. Ejecuta con: python3 clasificar.py

# PASO 1: este diccionario relaciona cada programa con su tipo.
# Ya hay tres hechos. Cambia cada "???" por el tipo correcto:
# "sistema", "aplicacion" o "desarrollo".
programas = {
    "Windows 11": "sistema",
    "Google Chrome": "aplicacion",
    "Visual Studio Code": "desarrollo",
    "Spotify": "???",
    "gcc": "???",
    "Driver de la tarjeta gráfica": "???",
    "Minecraft": "???",
    "Git": "???",
    "Linux Ubuntu": "???",
    "LibreOffice Writer": "???",
    "Depurador GDB": "???",
}

# PASO 2: crea un diccionario "grupos" con tres listas vacías,
# una para cada tipo: "sistema", "aplicacion" y "desarrollo".


# PASO 3: recorre el diccionario "programas" con un for
#     for nombre, tipo in programas.items():
# y añade cada nombre a la lista de su tipo con grupos[tipo].append(nombre).


# PASO 4: muestra cada grupo en una línea con este formato:
#   SISTEMA (3): Windows 11, Driver de la tarjeta gráfica, Linux Ubuntu
# Pista: ", ".join(lista) une los elementos de una lista con comas.
# Pista: len(lista) te da cuántos elementos tiene.
etiquetas = {"sistema": "SISTEMA", "aplicacion": "APLICACIÓN", "desarrollo": "DESARROLLO"}


# PASO 5: muestra el total de programas: "Total: 11 programas".

