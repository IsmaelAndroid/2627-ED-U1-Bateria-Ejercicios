# Ej22 · Boletín de notas
alumnos = [("Ana", 8.5), ("Luis", 4.2), ("Marta", 9.6), ("Pablo", 6.4), ("Sara", 5.0)]


def calificacion(nota):
    # PASO 1 (condicional): devuelve el texto de la calificación con if / elif / else:
    #   menos de 5 -> "Insuficiente"      menos de 6 -> "Suficiente"
    #   menos de 7 -> "Bien"              menos de 9 -> "Notable"
    #   9 o más    -> "Sobresaliente"
    return "?"


# PASO 2 (repetitiva for): recorre la lista y muestra cada alumno así:
#   Ana     8.5  Notable
# Pista: f"{nombre:<8}{nota:<5}{calificacion(nota)}"
# En el mismo bucle, ve sumando las notas y contando los aprobados (nota >= 5).


# PASO 3 (secuencial): calcula la media y muestra:
#   Media del grupo: 6.74
#   Aprobados: 4 de 5


# PASO 4 (repetitiva while): pide la nota de un alumno nuevo con input() y float().
# MIENTRAS la nota no esté entre 0 y 10, muestra "Nota no válida, inténtalo otra vez."
# y vuelve a pedirla. Cuando sea válida, muestra:  Alumno nuevo: 7.0  Notable
# Pista: empieza con  nota = -1  para que el while entre la primera vez.

