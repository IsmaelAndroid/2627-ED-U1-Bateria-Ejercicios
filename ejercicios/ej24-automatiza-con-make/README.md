# Ej24 · Automatiza con `make` ⚙️

**Apartado 1.6 · Herramientas de construcción** · ⏱️ 40 min

> 🎯 En el ejercicio 07 tenías que escribir **tres órdenes** cada vez y acordarte de qué recompilar. `make` lo automatiza: lees las **reglas** de un fichero `Makefile` y **solo recompila lo que ha cambiado**.

Una regla de `Makefile` tiene esta forma:

```makefile
objetivo: dependencias
	orden que lo genera
```

> ⚠️ La línea de la orden **empieza por un tabulador**, no por espacios. Si ves `missing separator`, es eso.

Esta carpeta ya tiene el programa completo (`main.c`, `operaciones.c`, `operaciones.h`). Tú solo escribes el `Makefile`.

## Pasos

**PASO 1–4.** Completa [`Makefile`](Makefile) siguiendo los comentarios.

**PASO 5.** Construye y ejecuta:

```bash
cd ejercicios/ej24-automatiza-con-make
make
make run
```

**PASO 6.** Ejecuta `make` **otra vez** sin cambiar nada. ¿Qué dice?

**PASO 7.** Simula que modificas un módulo (`touch` cambia la fecha del fichero) y vuelve a construir:

```bash
touch operaciones.c
make
```

**PASO 8.** Limpia todo lo generado: `make clean` y `ls`.

**PASO 9.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

```text
$ make
gcc -Wall -c main.c -o main.o
gcc -Wall -c operaciones.c -o operaciones.o
gcc main.o operaciones.o -o calculadora
$ make
make: 'calculadora' is up to date.
$ touch operaciones.c && make
gcc -Wall -c operaciones.c -o operaciones.o
gcc main.o operaciones.o -o calculadora
```
