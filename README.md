# 🧰 Batería de ejercicios · Tema 1 · Entornos de Desarrollo

**Entornos de Desarrollo · 1º DAM / 1º DAW B** · IES Rafael Alberti · Curso 2026-27

> 🎯 **Para qué sirve:** son **30 ejercicios para aprender y repasar** el tema 1, *Introducción al desarrollo de software*. **No cuentan para nota.** Son tu entrenamiento para las prácticas y el examen.
>
> 📚 **Teoría:** [revilofe.github.io · Unidad 1](https://revilofe.github.io/section3/u01/), apartados 1.1 a 1.7.

Casi todos los ejercicios son **prácticos**: vas a compilar programas en C y Java, ejecutar Python, mirar «por dentro» lo que genera el compilador, usar el depurador, escribir requisitos… Cada ejercicio tiene su carpeta con:

- un **`README.md`** con el enunciado **paso a paso**;
- los **ficheros de partida**, con comentarios `# PASO 1`, `# PASO 2`… que te dicen qué escribir y dónde;
- a veces un **`RESPUESTAS.md`** para contestar con tus palabras lo que has observado.

---

## 🚀 Cómo empezar (elige una opción)

### Opción A · GitHub Codespaces (recomendada, no hay que instalar nada)

1. En la página de tu repositorio pulsa **`<> Code` → pestaña `Codespaces` → `Create codespace on main`**.
2. Se abre un VS Code en el navegador con **Linux, `gcc`, `java`, `python` y `make` ya instalados**.
3. Abre la terminal con **`Ctrl + ñ`** (o *Terminal → New Terminal*) y ya puedes trabajar.

> ⏱️ Cuando acabes la clase, cierra la pestaña. El codespace se para solo y lo recuperas la próxima vez desde el mismo botón.

### Opción B · En tu ordenador con VS Code

Necesitas **Git**, **Python 3**, un **JDK** (Java 17 o superior) y **gcc** (en Windows, [MSYS2](https://www.msys2.org/) o WSL). Clona el repositorio con `git clone URL`. Algunos ejercicios usan órdenes de Linux (`file`, `nm`, `ldd`…): si estás en Windows, hazlos en el Codespace.

---

## 📌 La regla de los commits

- **Un commit al terminar cada ejercicio**, con el número delante: `git commit -m "Ej07: compilación por módulos"`.
- **`git push` al final de cada clase**, para tener tu trabajo en GitHub y poder seguir en casa.
- No hace falta hacerlos en orden, pero **dentro de cada apartado van de más fácil a más difícil**.

```bash
git add .
git commit -m "Ej01: inventario del equipo"
git push
```

---

## 🗺️ Índice de ejercicios

| Nº | Ejercicio | Tipo | Apartado |
|---|---|---|---|
| **1.1** | **Software y hardware** | | |
| 01 | [Inventario de tu equipo](ejercicios/ej01-inventario-del-equipo) | 🖥️ Terminal | 1.1 |
| 02 | [Clasifica el software](ejercicios/ej02-clasifica-el-software) | 🐍 Python | 1.1 |
| 03 | [RAM o disco: ¿qué sobrevive?](ejercicios/ej03-ram-o-disco) | 🐍 Python | 1.1 |
| 04 | [El sistema operativo como intermediario](ejercicios/ej04-el-so-intermediario) | 🐍 Python | 1.1 |
| **1.2** | **Código fuente, objeto y ejecutable** | | |
| 05 | [Tu primer programa en C, paso a paso](ejercicios/ej05-primer-programa-en-c) | ⚙️ C | 1.2 |
| 06 | [Mira dentro del código objeto](ejercicios/ej06-dentro-del-objeto) | ⚙️ C | 1.2 |
| 07 | [Compilación por módulos](ejercicios/ej07-compilacion-por-modulos) | ⚙️ C | 1.2 |
| 08 | [¿Error de compilación o de enlazado?](ejercicios/ej08-compilacion-o-enlazado) | ⚙️ C | 1.2 |
| 09 | [Enlazado estático y dinámico](ejercicios/ej09-estatico-y-dinamico) | ⚙️ C | 1.2 |
| **1.3** | **Código intermedio y máquinas virtuales** | | |
| 10 | [De `.java` a `.class`](ejercicios/ej10-de-java-a-class) | ☕ Java | 1.3 |
| 11 | [Lee el bytecode con `javap`](ejercicios/ej11-lee-el-bytecode) | ☕ Java | 1.3 |
| 12 | [Python también tiene bytecode](ejercicios/ej12-bytecode-de-python) | 🐍 Python | 1.3 |
| 13 | [Write once, run anywhere](ejercicios/ej13-write-once-run-anywhere) | ☕ Java + ⚙️ C | 1.3 |
| **1.4** | **Traductores: compiladores e intérpretes** | | |
| 14 | [Las cuatro etapas de `gcc`](ejercicios/ej14-etapas-de-gcc) | ⚙️ C | 1.4 |
| 15 | [Construye un analizador léxico](ejercicios/ej15-analizador-lexico) | 🐍 Python | 1.4 |
| 16 | [Léxico, sintáctico o semántico](ejercicios/ej16-tipos-de-error) | ⚙️ C | 1.4 |
| 17 | [Compilado contra interpretado: carrera](ejercicios/ej17-carrera-compilado-interpretado) | ⚙️ C + 🐍 Python | 1.4 |
| 18 | [El calentamiento del JIT](ejercicios/ej18-calentamiento-jit) | ☕ Java | 1.4 |
| **1.5** | **Lenguajes de programación** | | |
| 19 | [El mismo programa en tres lenguajes](ejercicios/ej19-tres-lenguajes) | 🐍 ☕ ⚙️ | 1.5 |
| 20 | [Caza de errores en Python](ejercicios/ej20-caza-de-errores) | 🐍 Python | 1.5 |
| 21 | [Tres paradigmas, un problema](ejercicios/ej21-tres-paradigmas) | 🐍 Python | 1.5 |
| 22 | [Estructuras de control](ejercicios/ej22-estructuras-de-control) | 🐍 Python | 1.5 |
| **1.6** | **Herramientas del desarrollo** | | |
| 23 | [Usa el depurador](ejercicios/ej23-usa-el-depurador) | 🐍 Python + VS Code | 1.6 |
| 24 | [Automatiza con `make`](ejercicios/ej24-automatiza-con-make) | ⚙️ C | 1.6 |
| 25 | [Biblioteca o framework](ejercicios/ej25-biblioteca-o-framework) | 🐍 Python | 1.6 |
| 26 | [Pruebas automáticas](ejercicios/ej26-pruebas-automaticas) | 🐍 Python | 1.6 |
| **1.7** | **Proceso de desarrollo** | | |
| 27 | [Escribe los requisitos](ejercicios/ej27-escribe-los-requisitos) | 📝 Análisis | 1.7 |
| 28 | [Del requisito al código](ejercicios/ej28-del-requisito-al-codigo) | 🐍 Python | 1.7 |
| 29 | [Los cuatro mantenimientos](ejercicios/ej29-cuatro-mantenimientos) | 🐍 Python + Git | 1.7 |
| 30 | [Un mini-Sprint en GitHub](ejercicios/ej30-mini-sprint) | 🐍 Python + GitHub | 1.7 |

---

## 🆘 Si te atascas

1. Vuelve a leer el paso: casi siempre la pista está en el comentario.
2. Lee **el mensaje de error entero**. Suele decir el fichero y la línea.
3. Consulta el apartado de teoría que aparece en la tabla.
4. Pregunta a tu compañero o compañera y, después, al profesor.
