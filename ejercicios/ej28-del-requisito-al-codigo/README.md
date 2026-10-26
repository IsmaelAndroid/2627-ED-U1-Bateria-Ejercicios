# Ej28 · Del requisito al código 🐍

**Apartado 1.7 · Ciclo de vida del software** · ⏱️ 60 min

> 🎯 Recorrer **las fases del ciclo de vida** con un programa pequeño: **análisis → diseño → codificación → pruebas**, dejando **un commit al final de cada fase**. Así tu historial de Git contará cómo se hizo el programa.

## Los requisitos (te los da el cliente)

| ID | Requisito |
|---|---|
| RF-01 | El sistema calculará la nota final de ED como el **70 % del examen + el 30 % de las prácticas** |
| RF-02 | Si la nota del examen es **menor que 4**, la nota final será como mucho **4**, aunque la media salga más alta |
| RF-03 | La nota final se redondeará a **1 decimal** |
| RF-04 | El sistema mostrará la calificación en texto: Insuficiente (< 5), Suficiente (< 6), Bien (< 7), Notable (< 9) o Sobresaliente |
| RNF-01 | El programa no usará bibliotecas externas |
| RNF-02 | Cada requisito funcional tendrá al menos una prueba automática |

## Pasos

### Fase 1 · Análisis

**PASO 1.** Abre [`analisis-y-diseno.md`](analisis-y-diseno.md) y completa la **tabla de casos**: para cada pareja de notas, calcula **a mano** el resultado que debería dar.

```bash
git add . && git commit -m "Análisis: casos de la nota final"
```

### Fase 2 · Diseño

**PASO 2.** En el mismo fichero, decide **qué funciones** tendrá el programa: nombre, qué reciben, qué devuelven y qué requisito cumplen. (Ya hay una de ejemplo.)

```bash
git commit -am "Diseño: funciones del programa"
```

### Fase 3 · Codificación

**PASO 3.** Programa las funciones en [`nota_final.py`](nota_final.py) según tu diseño y ejecútalo: `python3 nota_final.py`.

```bash
git commit -am "Codificación: cálculo de la nota final"
```

### Fase 4 · Pruebas

**PASO 4.** Completa [`test_nota_final.py`](test_nota_final.py) con **los casos de tu tabla del análisis**. Ejecuta `python3 -m unittest -v`. Si algo falla, corrige y vuelve a probar.

```bash
git commit -am "Pruebas: casos de la tabla de análisis"
```

**PASO 5.** Mira tu historial: `git log --oneline`.

## ✅ Comprueba

```text
$ python3 nota_final.py
Examen 8 · Prácticas 6 -> 7.4 Notable
Examen 3 · Prácticas 10 -> 4.0 Insuficiente
Examen 5 · Prácticas 5 -> 5.0 Suficiente
Examen 10 · Prácticas 10 -> 10.0 Sobresaliente
$ python3 -m unittest -v
...
OK
```
