# Ej27 · Escribe los requisitos 📝

**Apartado 1.7 · Análisis de requisitos** · ⏱️ 45 min

> 🎯 Hacer de **analista**: leer lo que pide un cliente, separar los **requisitos funcionales** (qué hace el sistema) de los **no funcionales** (cómo de bien lo hace, con qué restricciones) y escribirlos en una pequeña **ERS** (Especificación de Requisitos del Software).

| Tipo | Responde a… | Ejemplo |
|---|---|---|
| **Funcional (RF)** | ¿Qué **hace** el sistema? | «El sistema permitirá reservar una pista» |
| **No funcional (RNF)** | ¿**Cómo** lo hace? ¿Con qué calidad o restricciones? | «La reserva se confirmará en menos de 2 segundos» |

## El cliente dice…

> «Soy la jefa del departamento de Educación Física. En los recreos, el alumnado se pelea por las pistas de fútbol, baloncesto y pádel. Queremos una **aplicación web** para que los alumnos **reserven una pista** para un recreo concreto, como mucho **una reserva por alumno y día**. Tienen que **entrar con su usuario del instituto**. Los profesores de guardia deben poder **ver las reservas del día** y **anular** una si hay un problema. Debe funcionar **bien en el móvil**, porque es lo que usan, y estar disponible **desde las 8:00 hasta las 14:30**. Ah, y que **no se guarden más datos personales de los necesarios**, por la protección de datos.»

## Pasos

**PASO 1.** Subraya (mentalmente o en papel) cada **cosa que debe hacer** la aplicación y cada **condición de calidad o restricción**.

**PASO 2.** Clasifica las 10 frases de la **parte A** de [`ers.md`](ers.md).

**PASO 3.** Escribe en la **parte B** al menos **6 requisitos funcionales** y **4 no funcionales** del cliente, con un identificador (`RF-01`, `RNF-01`…) y su prioridad.

**PASO 4.** Contesta la **parte C**.

## ✅ Comprueba

- Cada requisito es **una sola cosa**, **verificable** (se puede comprobar si se cumple) y está escrito como «El sistema…».
- Ningún requisito habla de **cómo programarlo** (Python, base de datos…): eso es **diseño**, no análisis.
