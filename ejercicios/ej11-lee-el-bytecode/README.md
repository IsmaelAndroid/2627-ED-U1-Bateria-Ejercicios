# Ej11 · Lee el bytecode con `javap` ☕

**Apartado 1.3 · Código intermedio** · ⏱️ 30 min

> 🎯 Mirar **dentro** de un `.class` con `javap -c`, que **desensambla** el bytecode, y reconocer las instrucciones de la JVM que corresponden a tu código.

| Instrucción | Qué hace en la JVM |
|---|---|
| `iload_0`, `iload_1` | Mete en la pila el entero del parámetro 0, 1… |
| `iadd`, `imul` | Saca dos enteros de la pila, los suma (multiplica) y deja el resultado |
| `ireturn` | Devuelve el entero de la cima de la pila |
| `invokestatic` | Llama a un método estático |
| `bipush 10` | Mete el número 10 en la pila |

## Pasos

**PASO 1–2.** Completa [`Calculos.java`](Calculos.java).

**PASO 3.** Compila, ejecuta y desensambla:

```bash
cd ejercicios/ej11-lee-el-bytecode
javac Calculos.java
java Calculos
javap -c Calculos
```

**PASO 4.** Busca en la salida de `javap -c` el método `sumar` y el método `area`. Cópialos en [`RESPUESTAS.md`](RESPUESTAS.md) y contesta.

## ✅ Comprueba

```text
$ java Calculos
3 + 4 = 7
Área de 5 x 6 = 30
```

Y en `javap -c Calculos`, el método `sumar` es:

```text
  static int sumar(int, int);
    Code:
       0: iload_0
       1: iload_1
       2: iadd
       3: ireturn
```
