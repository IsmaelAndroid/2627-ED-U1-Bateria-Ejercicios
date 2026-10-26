# Ej30 · Un mini-Sprint en GitHub 🐍 🏃

**Apartado 1.7 · Metodologías ágiles: Scrum** · ⏱️ 2 sesiones

> 🎯 Vivir un **Sprint** de Scrum en pequeño, usando lo que ofrece GitHub: el **Product Backlog** serán **Issues**, el tablero será un **Project** y cada historia terminada cerrará su issue con un **commit**.

| Scrum | En GitHub |
|---|---|
| Historia de usuario | Un **Issue** |
| Product Backlog (todas las historias, ordenadas) | La lista de **Issues** abiertos |
| Tablero del Sprint | Un **Project** con columnas *Todo*, *In Progress* y *Done* |
| Incremento | El código que funciona al final del Sprint |
| Sprint Review y Retrospectiva | El fichero [`sprint.md`](sprint.md) |

El producto: una **lista de tareas** para organizar los deberes ([`tareas.py`](tareas.py)).

## Pasos

### 1 · Product Backlog

**PASO 1.** En tu repositorio de GitHub, ve a la pestaña **Issues → New issue** y crea **una issue por historia de usuario**:

| # | Título de la issue | Criterio de aceptación (escríbelo en la descripción) |
|---|---|---|
| 1 | Como alumno, quiero **añadir** una tarea | Se añade al final de la lista sin marcar |
| 2 | Como alumno, quiero **ver** mis tareas numeradas | Se ven con número, `[ ]` o `[x]` y el texto |
| 3 | Como alumno, quiero **marcar** una tarea como hecha | Pasa de `[ ]` a `[x]` |
| 4 | Como alumno, quiero **borrar** una tarea | Desaparece y las demás se renumeran |
| 5 | Como alumno, quiero ver **cuántas me quedan** | Muestra «Pendientes: N de M» |

> ⚠️ Fíjate en el **número** que GitHub da a cada issue (`#1`, `#2`…). Si ya tenías otras issues, los números serán distintos: usa los tuyos en los commits.

### 2 · Sprint Planning

**PASO 2.** Crea un tablero: pestaña **Projects → Link a project → New project → Board**. Añade las 5 issues a la columna **Todo**.

**PASO 3.** Elige **3 historias** para este Sprint y apúntalas en el **Sprint Backlog** de [`sprint.md`](sprint.md), con el **objetivo del Sprint**.

### 3 · El Sprint

**PASO 4.** Para cada historia: muévela a **In Progress**, prográmala en `tareas.py` (sigue los comentarios), ejecútala con `python3 tareas.py` y haz commit **cerrando la issue** con su número:

```bash
git commit -am "Añade tareas a la lista (closes #1)"
git push
```

GitHub cierra la issue al recibir el push. Muévela a **Done**.

### 4 · Review y Retrospectiva

**PASO 5.** Completa la **Sprint Review** (qué se ha terminado) y la **Retrospectiva** (qué ha ido bien, qué mejorar) en `sprint.md`. Las historias que no hayas hecho vuelven al backlog para el siguiente Sprint.

## ✅ Comprueba

Con las 5 historias hechas, `python3 tareas.py` muestra:

```text
1. [x] Ejercicios del tema 1 de ED
2. [ ] Estudiar para el examen
3. [ ] Práctica de GitHub
Pendientes: 2 de 3
```

Y en GitHub, las issues terminadas aparecen **cerradas** con un enlace al commit que las cerró.
