# Ej14 · Las cuatro etapas de `gcc` ⚙️

**Apartado 1.4 · Traductores** · ⏱️ 35 min

> 🎯 `gcc hola.c -o hola` parece un solo paso, pero por dentro hace **cuatro**. Vas a pararlo después de cada uno para ver qué genera.

```text
 circulo.c ─(1) preprocesar─▶ circulo.i ─(2) compilar─▶ circulo.s ─(3) ensamblar─▶ circulo.o ─(4) enlazar─▶ circulo
  fuente       gcc -E          fuente "expandido"  gcc -S   ensamblador   gcc -c   código objeto    gcc    ejecutable
```

## Pasos

**PASO 1.** Completa [`circulo.c`](circulo.c). Usa `#define`, una instrucción **del preprocesador**.

**PASO 2. Preprocesar** (`-E`): sustituye los `#define` y pega el contenido de los `#include`.

```bash
cd ejercicios/ej14-etapas-de-gcc
gcc -E circulo.c -o circulo.i
wc -l circulo.c circulo.i
tail -15 circulo.i
```

**PASO 3. Compilar a ensamblador** (`-S`): traduce a instrucciones del procesador, todavía en texto.

```bash
gcc -S circulo.c -o circulo.s
grep -n "call" circulo.s
```

**PASO 4. Ensamblar** (`-c`): convierte el ensamblador en código máquina (binario).

```bash
gcc -c circulo.s -o circulo.o
file circulo.o
```

**PASO 5. Enlazar** y ejecutar:

```bash
gcc circulo.o -o circulo
./circulo
```

**PASO 6.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

```text
$ ./circulo
Radio 2.0 -> área 12.57 y perímetro 12.57
Radio 5.0 -> área 78.54 y perímetro 31.42
```
