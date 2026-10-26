# Ej05 · Tu primer programa en C, paso a paso ⚙️

**Apartado 1.2 · Código fuente, objeto y ejecutable** · ⏱️ 30 min

> 🎯 Ver con tus ojos los **tres tipos de código**: escribes el **fuente** (`hola.c`), el compilador genera el **objeto** (`hola.o`) y el enlazador genera el **ejecutable** (`hola`).

```text
 hola.c ──gcc -c──▶ hola.o ──gcc (enlazar)──▶ hola ──./hola──▶ ¡se ejecuta!
 fuente             objeto                    ejecutable
```

## Pasos

**PASO 1–3.** Completa [`hola.c`](hola.c) siguiendo los comentarios.

**PASO 4. Compila sin enlazar.** La opción `-c` le dice a `gcc` que **solo compile**:

```bash
cd ejercicios/ej05-primer-programa-en-c
gcc -c hola.c -o hola.o
```

**PASO 5. Enlaza** el objeto con las bibliotecas para crear el ejecutable:

```bash
gcc hola.o -o hola
```

**PASO 6. Ejecuta:**

```bash
./hola
```

**PASO 7. Compara los tres ficheros.** La orden `file` dice qué tipo de fichero es cada uno, y `ls -l` su tamaño:

```bash
file hola.c hola.o hola
ls -l hola.c hola.o hola
```

**PASO 8.** Intenta abrir `hola.o` en VS Code. ¿Se puede leer?

**PASO 9.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

```text
$ ./hola
Hola, Ana. Este es mi primer programa en C
```

`file` dice algo como `hola.c: C source`, `hola.o: ELF 64-bit LSB relocatable` y `hola: ELF 64-bit LSB pie executable`.

> 📌 `hola.o` y `hola` **no se suben** a GitHub (están en `.gitignore`): se pueden volver a generar. Solo se sube el fuente.
