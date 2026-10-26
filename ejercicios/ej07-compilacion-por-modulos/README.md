# Ej07 · Compilación por módulos ⚙️

**Apartado 1.2 · Código fuente, objeto y ejecutable** · ⏱️ 40 min

> 🎯 Dividir un programa en **varios ficheros** (módulos), compilar cada uno a su código objeto y **enlazarlos** en un único ejecutable. Después comprobarás que, si cambias un módulo, **solo hay que recompilar ese**.

```text
 main.c        ──gcc -c──▶ main.o        ─┐
                                           ├──gcc (enlazar)──▶ calculadora
 operaciones.c ──gcc -c──▶ operaciones.o ─┘
        ▲
 operaciones.h  (la "lista" de funciones que main puede usar)
```

## Pasos

**PASO 1.** Lee [`operaciones.h`](operaciones.h): ya está hecho. Es la **cabecera**: declara las funciones, pero no tiene su código.

**PASO 2.** Completa [`operaciones.c`](operaciones.c) con el código de las cuatro funciones.

**PASO 3.** Completa [`main.c`](main.c) para que use las funciones.

**PASO 4.** Compila **cada módulo por separado** y después enlaza:

```bash
cd ejercicios/ej07-compilacion-por-modulos
gcc -c operaciones.c -o operaciones.o
gcc -c main.c -o main.o
gcc main.o operaciones.o -o calculadora
./calculadora
```

**PASO 5.** Mira la hora de los ficheros objeto: `ls -l --time-style=+%H:%M:%S *.o`

**PASO 6.** Cambia **solo** `operaciones.c`: haz que `dividir` devuelva `0` cuando el divisor sea `0`, en lugar de fallar. Ahora recompila **solo ese módulo** y vuelve a enlazar:

```bash
gcc -c operaciones.c -o operaciones.o
gcc main.o operaciones.o -o calculadora
./calculadora
ls -l --time-style=+%H:%M:%S *.o
```

**PASO 7.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

```text
$ ./calculadora
12 + 4 = 16
12 - 4 = 8
12 * 4 = 48
12 / 4 = 3
12 / 0 = 0
```
