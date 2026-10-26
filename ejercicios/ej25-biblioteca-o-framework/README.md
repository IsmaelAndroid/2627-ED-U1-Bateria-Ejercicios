# Ej25 · Biblioteca o framework 🐍

**Apartado 1.6 · Bibliotecas y frameworks** · ⏱️ 40 min

> 🎯 Entender la diferencia clave: con una **biblioteca**, **tu código la llama** cuando quiere. Con un **framework**, **el framework llama a tu código** cuando le toca. Eso se llama **inversión de control**.

```text
 BIBLIOTECA:   tu programa ──llama──▶ statistics.mean(notas)      (tú mandas)
 FRAMEWORK:    mini_framework ──llama──▶ tu_app.al_recibir(...)   (manda el framework)
```

## Parte A · Usar una biblioteca

**PASO 1.** Completa [`con_biblioteca.py`](con_biblioteca.py) usando las bibliotecas `statistics` y `random` de Python.

```bash
cd ejercicios/ej25-biblioteca-o-framework
python3 con_biblioteca.py
```

## Parte B · Usar un framework

[`mini_framework.py`](mini_framework.py) es un framework de juguete para hacer **chatbots**. **No lo cambies**: léelo. Su función `arrancar(app)` controla el flujo: llama a `al_iniciar()`, después a `al_recibir(mensaje)` por cada mensaje y por último a `al_terminar()`.

**PASO 2.** Completa [`mi_bot.py`](mi_bot.py): tú solo escribes **qué pasa** en cada momento. **Cuándo** pasa lo decide el framework.

```bash
python3 mi_bot.py
```

**PASO 3.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

```text
$ python3 con_biblioteca.py
Media: 7.00
Mediana: 7
Desviación típica: 1.58
Sale a la pizarra: Marta          ← cambia en cada ejecución

$ python3 mi_bot.py
[framework] Arrancando la aplicación...
Bot: ¡Hola! Soy el bot de ED.
Tú: hola
Bot: ¡Hola! ¿Qué tal?
Tú: ¿cuándo es el examen?
Bot: El examen del tema 1 es el viernes.
Tú: adiós
Bot: No te entiendo, prueba con "examen" o "hola".
Bot: Hasta luego. He respondido 3 mensajes.
[framework] Aplicación terminada.
```
