# Ej19 · El mismo programa en tres lenguajes 🐍 ☕ ⚙️

**Apartado 1.5 · Lenguajes de programación** · ⏱️ 45 min

> 🎯 Escribir **el mismo algoritmo** en Python, Java y C y comparar su **sintaxis**, cómo se **declaran los datos** y cómo se **ejecutan**.

**El algoritmo:** dada la lista de notas `6.5, 8, 4.5, 9, 7`, calcula la **media** y cuenta cuántas son **aprobadas** (≥ 5).

```text
1. suma = 0, aprobadas = 0
2. Para cada nota de la lista:
     suma = suma + nota
     si nota >= 5: aprobadas = aprobadas + 1
3. media = suma / número de notas
4. Mostrar la media con 2 decimales y las aprobadas
```

## Pasos

**PASO 1.** Completa [`media.py`](media.py) y ejecútalo: `python3 media.py`

**PASO 2.** Completa [`Media.java`](Media.java), compílalo y ejecútalo: `javac Media.java && java Media`

**PASO 3.** Completa [`media.c`](media.c), compílalo y ejecútalo: `gcc media.c -o media && ./media`

**PASO 4.** Rellena la tabla comparativa de [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

Los **tres** programas muestran exactamente:

```text
Media: 7.00
Aprobadas: 4 de 5
```
