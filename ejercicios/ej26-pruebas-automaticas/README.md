# Ej26 · Pruebas automáticas 🐍 🧪

**Apartado 1.6 · Herramientas de prueba** · ⏱️ 45 min

> 🎯 Escribir **pruebas unitarias** con `unittest` (la herramienta de Python equivalente a **JUnit** en Java) para comprobar automáticamente que unas funciones hacen lo que deben. Las pruebas van a encontrar **un error** escondido.

[`tienda.py`](tienda.py) tiene dos funciones:

- `precio_con_iva(precio, tipo)`: suma el IVA. Tipos: `"general"` (21 %), `"reducido"` (10 %) y `"superreducido"` (4 %).
- `aplicar_descuento(precio, porcentaje)`: resta un porcentaje. Si el porcentaje no está entre 0 y 100, lanza `ValueError`.

**Una de las dos tiene un fallo.** No lo busques leyendo: deja que lo encuentren las pruebas.

## Pasos

**PASO 1.** Abre [`test_tienda.py`](test_tienda.py). La primera prueba ya está hecha: léela. Ejecuta las pruebas:

```bash
cd ejercicios/ej26-pruebas-automaticas
python3 -m unittest -v
```

**PASO 2–6.** Escribe las otras pruebas siguiendo los comentarios y vuelve a ejecutar. Alguna **fallará** (`FAIL`).

**PASO 7.** Lee el mensaje del fallo: te dice qué valor esperabas y cuál se ha obtenido. **Arregla `tienda.py`** (no la prueba) y ejecuta las pruebas otra vez hasta que todas pasen.

**PASO 8.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

```text
test_descuento_cero ... ok
test_descuento_del_20 ... ok
test_descuento_no_valido ... ok
test_iva_general ... ok
test_iva_reducido ... ok
test_iva_superreducido ... ok
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```
