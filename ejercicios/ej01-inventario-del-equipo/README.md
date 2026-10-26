# Ej01 · Inventario de tu equipo 🖥️

**Apartado 1.1 · Software y hardware** · ⏱️ 20 min

> 🎯 Vas a preguntarle al sistema operativo qué **hardware** tiene la máquina y qué **software** hay instalado, y a clasificar cada cosa.

## Pasos

**PASO 1.** Abre la terminal (`Ctrl + ñ`) del Codespace y ejecuta estas órdenes, una a una. Lee la salida con calma.

```bash
lscpu | head -20      # el procesador (CPU): modelo, núcleos, arquitectura
free -h               # la memoria RAM: total, usada, libre
df -h /               # el disco: tamaño y espacio libre
uname -a              # el sistema operativo y su núcleo (kernel)
cat /etc/os-release   # nombre y versión de la distribución Linux
```

> 💡 Si trabajas en Windows sin Codespace, usa `systeminfo` en la terminal y el *Administrador de tareas → Rendimiento*.

**PASO 2.** Abre [`inventario.md`](inventario.md) y rellena la **tabla 1** con los datos que has obtenido.

**PASO 3.** Ahora mira qué software de desarrollo tiene la máquina:

```bash
python3 --version
gcc --version | head -1
java -version
git --version
```

Rellena la **tabla 2** de `inventario.md`.

**PASO 4.** Contesta las dos preguntas del final de `inventario.md`.

## ✅ Comprueba

- La tabla 1 tiene **CPU, núcleos, arquitectura, RAM, disco y sistema operativo**.
- Has clasificado cada elemento como **hardware** o **software**.

**PASO 5.** Haz commit: `git add . && git commit -m "Ej01: inventario del equipo"`.
