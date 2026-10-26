# Ej23 · Usa el depurador 🐍 🐞

**Apartado 1.6 · Herramientas: el depurador** · ⏱️ 40 min

> 🎯 Encontrar **dos errores lógicos** usando el **depurador de VS Code**: puntos de interrupción, ejecución paso a paso y el panel de variables. **Prohibido** llenar el código de `print`: hay que encontrarlos depurando.

[`temperaturas.py`](temperaturas.py) calcula la **media** y la **máxima** de las temperaturas de una semana de invierno. No da ningún error… pero los resultados están **mal**.

| Tecla en VS Code | Qué hace |
|---|---|
| Clic a la izquierda del número de línea | Pone un **punto de interrupción** (punto rojo 🔴) |
| `F5` | Empieza a depurar y se para en el primer punto de interrupción |
| `F10` | **Paso a paso por encima**: ejecuta la línea sin entrar en las funciones |
| `F11` | **Paso a paso hacia dentro**: entra en la función de esa línea |
| `Mayús + F5` | Para la depuración |

## Pasos

**PASO 1.** Ejecuta el programa normal y mira los resultados: `python3 temperaturas.py`. ¿Cuál debería ser la media de `-3, -7, -1, -5, -4`? Calcúlala a mano.

**PASO 2.** Pon un punto de interrupción en la primera línea de la función `media` (`total = 0`).

**PASO 3.** Pulsa **`F5`** y elige **Python Debugger → Python File**. El programa se para en tu punto rojo.

**PASO 4.** Pulsa **`F10`** varias veces y mira el panel **VARIABLES** (a la izquierda): fíjate en `i`, `total` y en **qué temperaturas se van sumando**. ¿Se suman todas?

**PASO 5.** Haz lo mismo con la función `maxima`: mira el valor inicial de `mayor` y cómo cambia. En el panel **WATCH** (inspección) añade la expresión `t > mayor`.

**PASO 6.** Corrige los dos errores, vuelve a ejecutar y rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

```text
Temperaturas: [-3, -7, -1, -5, -4]
Media: -4.00 ºC
Máxima: -1 ºC
```
