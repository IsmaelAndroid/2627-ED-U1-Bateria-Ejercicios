# Ej15 · Analizador léxico de un mini-lenguaje

RESERVADAS = {"si", "entonces", "mientras", "mostrar"}
OPERADORES = {"+", "-", "*", "/", "=", ">", "<"}


def tipo_de_token(palabra):
    # PASO 1: devuelve el tipo de la palabra siguiendo la tabla del README.
    # ¡El orden importa! Comprueba primero si es RESERVADA (porque "si" también
    # cumple isidentifier()), luego NUMERO, IDENTIFICADOR y OPERADOR.
    # Si no es nada de eso, devuelve "ERROR".
    return "ERROR"


def analizar(codigo):
    # PASO 2: separa el código en palabras con codigo.split() y devuelve una lista
    # de parejas (tipo, palabra). Ejemplo: [("RESERVADA", "si"), ("IDENTIFICADOR", "precio")]
    tokens = []

    return tokens


def mostrar_tokens(codigo):
    print(f"Código: {codigo}")
    tokens = analizar(codigo)
    # PASO 3: muestra cada token con el tipo alineado a 15 caracteres:
    #     print(f"  {tipo:<15}{palabra}")


    # PASO 4: cuenta los tokens de tipo "ERROR" y muestra el resumen:
    #   Tokens: 10 · Errores léxicos: 0


    print()


mostrar_tokens("si precio > 100 entonces total = precio * 2")
mostrar_tokens("mostrar 3x @ nota")
