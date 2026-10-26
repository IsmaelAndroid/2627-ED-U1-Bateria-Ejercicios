# Ej16 · Léxico, sintáctico o semántico ⚙️

**Apartado 1.4 · Fases del compilador** · ⏱️ 30 min

> 🎯 El compilador analiza el código en **tres fases** y cada una detecta un tipo de error distinto. Vas a provocar uno de cada y aprender a reconocerlos por el mensaje.

| Fase | Comprueba… | Ejemplo de error |
|---|---|---|
| **Léxica** | que cada «palabra» (token) es válida | un símbolo que no existe en el lenguaje |
| **Sintáctica** | que los tokens siguen la gramática | falta un paréntesis o un `;` |
| **Semántica** | que el programa tiene sentido | usar una variable que no está declarada |

En la carpeta hay **tres programas con un error cada uno**: `error_a.c`, `error_b.c` y `error_c.c`.

## Pasos

**PASO 1.** Compila cada uno y lee **con calma** el mensaje:

```bash
cd ejercicios/ej16-tipos-de-error
gcc -c error_a.c
gcc -c error_b.c
gcc -c error_c.c
```

**PASO 2.** En [`RESPUESTAS.md`](RESPUESTAS.md), indica para cada uno **la línea**, **el mensaje** y **la fase** que lo detecta.

**PASO 3.** Arregla los tres (los comentarios te dicen qué debe hacer cada programa) y comprueba que compilan y funcionan:

```bash
gcc error_a.c -o a && ./a
gcc error_b.c -o b && ./b
gcc error_c.c -o c && ./c
```

## ✅ Comprueba

```text
$ ./a
Resultado: 15
$ ./b
Aprobado
$ ./c
Total: 24.00
```
