# Ej12 · Python también tiene bytecode 🐍

**Apartados 1.3 y 1.4 · Código intermedio e intérpretes** · ⏱️ 25 min

> 🎯 Se suele decir que Python «se interpreta línea a línea». No es del todo así: **CPython primero compila tu código a bytecode** y después su máquina virtual ejecuta ese bytecode. Vas a verlo.

## Pasos

**PASO 1.** Completa [`notas.py`](notas.py) (una función que calcula si una nota está aprobada).

**PASO 2.** Completa [`ver_bytecode.py`](ver_bytecode.py): usa el módulo `dis` para mostrar el bytecode de tu función.

```bash
cd ejercicios/ej12-bytecode-de-python
python3 ver_bytecode.py
```

**PASO 3.** Pide a Python que compile `notas.py` y guarde el bytecode en disco:

```bash
python3 -m py_compile notas.py
ls __pycache__
file __pycache__/*.pyc
```

**PASO 4.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

`python3 ver_bytecode.py` muestra primero el resultado y luego instrucciones como:

```text
Nota 7.5 -> APROBADO
Nota 4 -> SUSPENSO
  ...  LOAD_FAST                nota
  ...  LOAD_CONST               5
  ...  COMPARE_OP               >= ...
  ...  RETURN_VALUE / RETURN_CONST
```
(Los nombres exactos cambian un poco según la versión de Python.)

En `__pycache__` aparece un fichero como `notas.cpython-312.pyc`.
