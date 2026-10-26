# Ej06 · Mira dentro del código objeto ⚙️

**Apartado 1.2 · Código fuente, objeto y ejecutable** · ⏱️ 30 min

> 🎯 Descubrir **qué le falta** a un código objeto para poder ejecutarse, y cómo el **enlazador** lo completa. Usarás `nm`, que lista los **símbolos** (nombres de funciones y variables) de un fichero.

| Letra en `nm` | Significa |
|---|---|
| `T` | La función **está definida aquí** (su código está en este fichero) |
| `U` | La función se usa pero **no está aquí** (*undefined*): alguien tiene que aportarla |

## Pasos

**PASO 1–2.** Completa [`saludo.c`](saludo.c): una función propia `doble` y un `main` que la use junto con `printf`.

**PASO 3.** Compila **sin enlazar** y mira los símbolos del objeto:

```bash
cd ejercicios/ej06-dentro-del-objeto
gcc -c saludo.c -o saludo.o
nm saludo.o
```

**PASO 4.** Enlaza y mira los símbolos del ejecutable (filtramos las líneas que interesan):

```bash
gcc saludo.o -o saludo
nm saludo | grep -E " main| doble|printf"
./saludo
```

**PASO 5.** Pregunta al sistema **qué bibliotecas** necesita el ejecutable al arrancar:

```bash
ldd saludo
```

**PASO 6.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

```text
$ nm saludo.o
0000000000000000 T doble
0000000000000014 T main
                 U printf
$ ./saludo
El doble de 21 es 42
```
