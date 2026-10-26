# Ej23 · temperaturas.py · Este programa tiene DOS errores lógicos. Encuéntralos con el depurador.


def media(temperaturas):
    total = 0
    for i in range(1, len(temperaturas)):
        total += temperaturas[i]
    return total / len(temperaturas)


def maxima(temperaturas):
    mayor = 0
    for t in temperaturas:
        if t > mayor:
            mayor = t
    return mayor


semana = [-3, -7, -1, -5, -4]
print(f"Temperaturas: {semana}")
print(f"Media: {media(semana):.2f} ºC")
print(f"Máxima: {maxima(semana)} ºC")
