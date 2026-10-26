# Ej21 · Tres paradigmas, un problema 🐍

**Apartado 1.5 · Paradigmas de programación** · ⏱️ 45 min

> 🎯 Resolver el **mismo problema** con tres **paradigmas** distintos, los tres en Python, para ver que un paradigma es una **forma de pensar** el programa.

**El problema:** en un carrito hay productos con estos precios: `12.5, 30, 8, 45, 22`. Los que cuestan **más de 20 €** tienen un **10 % de descuento**. ¿Cuánto hay que pagar?

| Paradigma | Idea | Cómo se nota en el código |
|---|---|---|
| **Imperativo** | Dices **paso a paso** qué hacer y vas cambiando variables | `for`, acumulador `total += …` |
| **Funcional** | **Compones funciones** que transforman datos sin modificarlos | funciones pequeñas, `map`, `sum`, sin variables que cambian |
| **Orientado a objetos** | Creas **objetos** que tienen **datos** y **métodos** | `class Carrito`, `self.productos`, `carrito.total()` |

## Pasos

Completa los tres ficheros y ejecuta cada uno:

```bash
cd ejercicios/ej21-tres-paradigmas
python3 imperativo.py
python3 funcional.py
python3 objetos.py
```

Después contesta en [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

Los tres muestran:

```text
Total a pagar: 107.80 €
```
