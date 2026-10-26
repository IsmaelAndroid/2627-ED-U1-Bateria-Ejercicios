# Ej17 · Compilado contra interpretado: carrera ⚙️ 🐍

**Apartado 1.4 · Compiladores e intérpretes** · ⏱️ 30 min

> 🎯 Escribir **el mismo cálculo** en C (compilado AOT a código máquina) y en Python (interpretado por una máquina virtual) y **medir** cuánto tarda cada uno con la orden `time`.

El cálculo: **sumar todos los números del 1 al 30 000 000**.

## Pasos

**PASO 1.** Completa [`suma.c`](suma.c) y [`suma.py`](suma.py).

**PASO 2.** Compila el de C y mide los dos. Fíjate en la línea `real` (tiempo total):

```bash
cd ejercicios/ej17-carrera-compilado-interpretado
gcc suma.c -o suma
time ./suma
time python3 suma.py
```

**PASO 3.** Prueba a compilar el de C **con optimización** (`-O2`) y mide otra vez:

```bash
gcc -O2 suma.c -o suma_rapida
time ./suma_rapida
```

**PASO 4.** Mide también cuánto tarda **solo la compilación**: `time gcc suma.c -o suma`.

**PASO 5.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

Los dos programas deben mostrar **el mismo resultado**:

```text
Suma de 1 a 30000000 = 450000015000000
```
