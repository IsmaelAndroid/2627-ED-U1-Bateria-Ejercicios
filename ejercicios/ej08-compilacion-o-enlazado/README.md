# Ej08 · ¿Error de compilación o de enlazado? ⚙️

**Apartado 1.2 · Código fuente, objeto y ejecutable** · ⏱️ 30 min

> 🎯 Aprender a distinguir **en qué etapa** falla un programa. Si sabes si el fallo es del **compilador** o del **enlazador**, sabrás dónde buscarlo.

| Etapa | Orden | Falla cuando… |
|---|---|---|
| Compilación | `gcc -c fichero.c` | el código no respeta las reglas del lenguaje |
| Enlazado | `gcc fichero.o -o programa` | falta el código de algo que se usa (una función, `main`…) |

En esta carpeta hay **tres programas con un fallo cada uno**: `roto1.c`, `roto2.c` y `roto3.c`. **No los arregles todavía.**

## Pasos

**PASO 1.** Para cada programa, primero **compila sin enlazar** y después **enlaza**. Anota en qué orden aparece el error:

```bash
cd ejercicios/ej08-compilacion-o-enlazado
gcc -c roto1.c -o roto1.o      # ¿falla aquí?
gcc roto1.o -o roto1           # ¿o aquí?
```

Repite con `roto2.c` y `roto3.c`.

**PASO 2.** Copia el mensaje de error en la tabla de [`RESPUESTAS.md`](RESPUESTAS.md) e indica la etapa.

**PASO 3.** Arregla los tres programas (lee los comentarios de cada uno) y comprueba que ya compilan, enlazan y se ejecutan.

## ✅ Comprueba

Al final, los tres se ejecutan:

```text
$ ./roto1
Total: 30
$ ./roto2
Precio con IVA: 121.00
$ ./roto3
Nota media: 7.50
```

> 💡 El enlazador suele decir `undefined reference to …` y menciona `ld` (*linker*). El compilador indica el fichero y la línea: `roto1.c:6:5: error: …`.
