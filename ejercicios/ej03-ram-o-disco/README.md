# Ej03 · RAM o disco: ¿qué sobrevive? 🐍

**Apartado 1.1 · Software y hardware** · ⏱️ 20 min

> 🎯 Comprobar con tus propios ojos que la **RAM es volátil** (los datos desaparecen cuando el programa termina) y que el **disco es persistente** (los datos se quedan).

Cuando un programa guarda algo en una **variable**, ese dato vive en la **RAM**. Cuando lo escribe en un **fichero**, va al **disco**.

## Pasos

**PASOS 1 a 4.** Completa [`contador.py`](contador.py) siguiendo los comentarios.

**PASO 5.** Ejecuta el programa **tres veces seguidas**:

```bash
cd ejercicios/ej03-ram-o-disco
python3 contador.py
python3 contador.py
python3 contador.py
```

**PASO 6.** Mira qué hay en el fichero `visitas.txt` que se ha creado: `cat visitas.txt`.

**PASO 7.** Contesta en [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

La tercera ejecución debe mostrar:

```text
Contador en RAM (variable): 1
Contador en disco (fichero): 3
```

Haz commit (el fichero `visitas.txt` también se sube).
