# Ej18 · El calentamiento del JIT ☕

**Apartado 1.4 · Compilación JIT** · ⏱️ 35 min

> 🎯 La JVM empieza **interpretando** el bytecode. Cuando detecta que un método se usa mucho (está «caliente»), lo **compila a código máquina** mientras el programa se ejecuta: es la compilación **JIT** (*Just-In-Time*). Por eso las primeras vueltas van más lentas: es el **calentamiento** (*warm-up*).

Vas a ejecutar **10 rondas** del mismo cálculo y medir cuánto tarda cada una.

## Pasos

**PASO 1–3.** Completa [`Calentamiento.java`](Calentamiento.java).

**PASO 4.** Ejecuta normal (con JIT):

```bash
cd ejercicios/ej18-calentamiento-jit
javac Calentamiento.java
java Calentamiento
```

**PASO 5.** Ahora ejecuta **sin JIT**, solo con el intérprete (`-Xint`):

```bash
java -Xint Calentamiento
```

**PASO 6.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

Con JIT, las primeras rondas tardan **más** que las últimas. Algo parecido a:

```text
Ronda 1: 25997 primos en 35 ms
Ronda 2: 25997 primos en 26 ms
Ronda 3: 25997 primos en 24 ms
...
Ronda 10: 25997 primos en 24 ms
```

Con `-Xint`, todas las rondas tardan parecido y **unas 10 veces más** (unos 240 ms cada una).
