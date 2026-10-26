# Ej29 · Los cuatro mantenimientos 🐍

**Apartado 1.7 · Mantenimiento del software** · ⏱️ 50 min

> 🎯 El software **ya entregado** también cambia. Vas a hacer **un cambio de cada tipo de mantenimiento** sobre una pequeña tienda, **un commit por cada uno**, para que se vea en el historial.

| Tipo | Para qué | En este ejercicio |
|---|---|---|
| **Correctivo** | Arreglar un **fallo** | El total del pedido sale mal |
| **Perfectivo** | **Mejorar** algo que ya funciona (claridad, rendimiento, presentación) | El ticket se ve feo y el código es poco claro |
| **Evolutivo** | Añadir una **funcionalidad nueva** que pide el cliente | Cupones de descuento |
| **Adaptativo** | **Adaptarse a un cambio externo** (ley, plataforma, sistema) | La tienda empieza a vender en Canarias, donde hay IGIC del 7 % en vez de IVA |

## Pasos

**PASO 0.** Ejecuta [`tienda.py`](tienda.py) y mira el resultado: `python3 tienda.py`. El pedido es 4 cuadernos (2,50 €), 5 bolis (0,80 €) y 1 mochila (25 €). ¿Cuánto debería costar sin IVA?

**PASO 1 · Correctivo.** Encuentra y corrige el fallo del total (sigue la pista del comentario `CORRECTIVO`).

```bash
git commit -am "Correctivo: el total sumaba solo el último producto"
```

**PASO 2 · Perfectivo.** Sigue el comentario `PERFECTIVO`: deja el ticket alineado y con dos decimales. El resultado no cambia, solo **mejora**.

```bash
git commit -am "Perfectivo: ticket alineado y con dos decimales"
```

**PASO 3 · Evolutivo.** Sigue el comentario `EVOLUTIVO`: añade el cupón `ED10` (10 % de descuento sobre el subtotal).

```bash
git commit -am "Evolutivo: cupón de descuento ED10"
```

**PASO 4 · Adaptativo.** Sigue el comentario `ADAPTATIVO`: el impuesto depende de la región (`peninsula`: IVA 21 %; `canarias`: IGIC 7 %).

```bash
git commit -am "Adaptativo: IGIC para pedidos de Canarias"
```

**PASO 5.** `git log --oneline` y rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

```text
$ python3 tienda.py
--- Pedido en la península ---
cuaderno     4 x  2.50 =  10.00
boli         5 x  0.80 =   4.00
mochila      1 x 25.00 =  25.00
Subtotal:                 39.00
IVA (21 %):                8.19
TOTAL:                    47.19
--- Pedido en la península con cupón ED10 ---
...
Descuento ED10:           -3.90
...
TOTAL:                    42.47
--- Pedido en Canarias ---
...
IGIC (7 %):                2.73
TOTAL:                    41.73
```
