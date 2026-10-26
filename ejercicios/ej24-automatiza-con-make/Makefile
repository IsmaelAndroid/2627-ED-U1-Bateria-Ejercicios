# Ej24 · Makefile de la calculadora
# Recuerda: las líneas de órdenes empiezan por TABULADOR.

# PASO 1: regla principal. El objetivo "calculadora" depende de main.o y operaciones.o
#         y se genera enlazándolos:
# calculadora: main.o operaciones.o
# <TAB>gcc main.o operaciones.o -o calculadora


# PASO 2: dos reglas para los objetos. main.o depende de main.c y de operaciones.h
#         (si cambia la cabecera, hay que recompilar main):
# main.o: main.c operaciones.h
# <TAB>gcc -Wall -c main.c -o main.o
#
#         Escribe tú la de operaciones.o (depende de operaciones.c y operaciones.h).


# PASO 3: regla "run" que primero construye la calculadora y después la ejecuta:
# run: calculadora
# <TAB>./calculadora


# PASO 4: regla "clean" que borra lo generado (no depende de nada):
# clean:
# <TAB>rm -f *.o calculadora
#
# Y al final, indica que run y clean no son ficheros:
# .PHONY: run clean
