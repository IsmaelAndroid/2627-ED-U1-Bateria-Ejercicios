# Ej09 · Enlazado estático y dinámico ⚙️

**Apartados 1.2 y 1.6 · Ejecutables y enlazado** · ⏱️ 25 min

> 🎯 Generar **el mismo programa** de dos formas y comparar: con enlazado **dinámico** (las bibliotecas se cargan al ejecutar) y **estático** (las bibliotecas van dentro del ejecutable). Después razonarás **dónde puede funcionar** un ejecutable.

## Pasos

**PASO 1.** Completa [`info.c`](info.c) siguiendo los comentarios.

**PASO 2.** Genera las dos versiones:

```bash
cd ejercicios/ej09-estatico-y-dinamico
gcc info.c -o info_dinamico
gcc -static info.c -o info_estatico
```

**PASO 3.** Compáralas:

```bash
ls -lh info_dinamico info_estatico
file info_dinamico info_estatico
ldd info_dinamico
ldd info_estatico
./info_dinamico
./info_estatico
```

**PASO 4.** Averigua la arquitectura de la máquina: `uname -m`.

**PASO 5.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

- `info_estatico` ocupa **mucho más** (cientos de KB) que `info_dinamico` (unos 16 KB).
- `ldd info_estatico` responde `not a dynamic executable`.
- Los dos muestran lo mismo:

```text
Programa compilado para Linux en x86_64
Raíz cuadrada de 2: 1.4142
```
