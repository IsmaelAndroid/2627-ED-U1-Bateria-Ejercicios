# Ej10 · De `.java` a `.class` ☕

**Apartado 1.3 · Código intermedio** · ⏱️ 25 min

> 🎯 Seguir el camino de un programa Java: el **fuente** (`.java`) se compila a **bytecode** (`.class`), que **no** entiende la CPU directamente: lo ejecuta la **máquina virtual de Java (JVM)**.

```text
 HolaMundo.java ──javac──▶ HolaMundo.class ──java (JVM)──▶ instrucciones de la CPU
 código fuente             bytecode (código intermedio)
```

## Pasos

**PASO 1–3.** Completa [`HolaMundo.java`](HolaMundo.java).

**PASO 4. Compila** con `javac` (el compilador de Java):

```bash
cd ejercicios/ej10-de-java-a-class
javac HolaMundo.java
ls -l
```

**PASO 5. Ejecuta** con `java` (arranca la JVM). Ojo: se pone el **nombre de la clase**, sin `.class`:

```bash
java HolaMundo
```

**PASO 6.** ¿Qué tipo de fichero es cada uno?

```bash
file HolaMundo.java HolaMundo.class
```

**PASO 7.** Intenta ejecutar el `.class` como si fuera un programa normal y fíjate en el error:

```bash
chmod +x HolaMundo.class
./HolaMundo.class
```

**PASO 8.** Rellena [`RESPUESTAS.md`](RESPUESTAS.md).

## ✅ Comprueba

```text
$ java HolaMundo
Hola desde la JVM
Sistema: Linux · Java 21.0.x
```
(La versión de Java puede ser otra.)
