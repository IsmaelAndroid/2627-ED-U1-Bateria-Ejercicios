# Ej04 · El sistema operativo como intermediario 🐍

**Apartado 1.1 · Software y hardware** · ⏱️ 25 min

> 🎯 Las aplicaciones **no tocan el hardware directamente**: se lo piden al sistema operativo. En Python eso se hace con los módulos `os` y `platform`. Vas a escribir un programa que **pide cosas al SO** y muestra lo que responde.

```text
 Tu programa  ──pide──▶   Sistema operativo  ──controla──▶  Hardware
 (Python)     ◀─responde─ (Linux / Windows)  ◀────────────  (CPU, disco…)
```

## Pasos

Completa [`pregunta_al_so.py`](pregunta_al_so.py) siguiendo los comentarios y ejecútalo:

```bash
cd ejercicios/ej04-el-so-intermediario
python3 pregunta_al_so.py
```

Después contesta en [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

La salida tiene **6 líneas** parecidas a estas (los valores dependen de tu máquina):

```text
Sistema operativo: Linux 6.5.0-1025-azure
Arquitectura: x86_64
Núcleos de CPU: 2
Carpeta actual: /workspaces/.../ej04-el-so-intermediario
Ficheros aquí: README.md, RESPUESTAS.md, pregunta_al_so.py, saludo.txt
Identificador de este proceso (PID): 12345
```

Y se ha creado el fichero `saludo.txt`. Haz commit.
