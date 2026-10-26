# Ej13 · Write once, run anywhere ☕ ⚙️

**Apartado 1.3 · Código intermedio y máquinas virtuales** · ⏱️ 30 min

> 🎯 Comparar un **ejecutable nativo** de C con un **`.class`** de Java para entender por qué el bytecode es **portable** y el ejecutable no. Lo verás mirando los **primeros bytes** de cada fichero (su «firma» o *número mágico*).

## Pasos

**PASO 1.** Completa [`Saludo.java`](Saludo.java) y [`saludo.c`](saludo.c): los dos muestran lo mismo.

**PASO 2.** Compila los dos:

```bash
cd ejercicios/ej13-write-once-run-anywhere
javac Saludo.java
gcc saludo.c -o saludo
java Saludo
./saludo
```

**PASO 3.** Mira los **4 primeros bytes** de cada fichero en hexadecimal:

```bash
head -c 4 Saludo.class | od -A n -t x1
head -c 4 saludo | od -A n -t x1 -c
```

**PASO 4.** Pregunta qué son:

```bash
file Saludo.class saludo
```

**PASO 5.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md), que incluye una tabla sobre otras máquinas virtuales.

## ✅ Comprueba

```text
$ head -c 4 Saludo.class | od -A n -t x1
 ca fe ba be
$ head -c 4 saludo | od -A n -t x1 -c
  7f  45  4c  46
 177   E   L   F
```

Sí: los ficheros `.class` empiezan por **CAFEBABE** 😄.
