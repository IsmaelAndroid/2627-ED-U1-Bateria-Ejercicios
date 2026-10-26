# Ej20 · Caza de errores en Python 🐍

**Apartado 1.5 · Léxico, sintaxis y semántica** · ⏱️ 35 min

> 🎯 Reconocer **qué tipo de error** es cada uno por el mensaje de Python y **en qué momento** aparece: antes de ejecutar nada (al compilar a bytecode) o durante la ejecución.

| Tipo de error | ¿Cuándo aparece? | Mensaje típico de Python |
|---|---|---|
| **Léxico** | Antes de ejecutar | `SyntaxError: unterminated string literal` |
| **Sintáctico** | Antes de ejecutar | `SyntaxError: invalid syntax`, `IndentationError` |
| **Semántico / de ejecución** | Al llegar a esa línea | `NameError`, `TypeError`, `ZeroDivisionError` |
| **Lógico** | Nunca da error | El programa funciona… pero el resultado está mal |

## Pasos

En [`errores.py`](errores.py) hay **6 bloques** comentados con un error cada uno.

**PASO 1.** **Descomenta solo el bloque 1** (quita los `#` de sus líneas de código), ejecuta y anota el mensaje:

```bash
cd ejercicios/ej20-caza-de-errores
python3 errores.py
```

**PASO 2.** Arregla el bloque 1 para que muestre lo que dice su comentario. Pasa al bloque 2 y repite… hasta el 6.

> 💡 En VS Code: selecciona las líneas y pulsa **`Ctrl + }`** (o `Ctrl + /`) para comentar o descomentar de golpe.

**PASO 3.** Rellena la tabla de [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

Con los 6 bloques descomentados y arreglados:

```text
1) Total: 7
2) Hola, Ana
3) Tendrás 21 años
4) Nota final: 8.5
5) Media por alumno: 0
6) Media de 6 y 8: 7.0
```
