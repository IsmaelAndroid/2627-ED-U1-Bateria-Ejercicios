# Ej15 · Construye un analizador léxico 🐍

**Apartado 1.4 · Fases del compilador** · ⏱️ 45 min

> 🎯 La **primera fase** de cualquier compilador es el **análisis léxico**: leer el texto y agruparlo en **tokens** (palabras con significado). Vas a programar un analizador léxico sencillo.

```text
 "si precio > 100 entonces total = precio * 2"
                       │  análisis léxico
                       ▼
 [RESERVADA si] [IDENTIFICADOR precio] [OPERADOR >] [NUMERO 100] [RESERVADA entonces] ...
```

Para simplificar, en nuestro mini-lenguaje **todos los tokens van separados por espacios**.

| Tipo de token | Regla |
|---|---|
| `RESERVADA` | Está en la lista de palabras reservadas: `si`, `entonces`, `mientras`, `mostrar` |
| `NUMERO` | Todo son dígitos (`"100".isdigit()`) |
| `IDENTIFICADOR` | Empieza por letra o `_` y solo tiene letras, dígitos o `_` (`"precio".isidentifier()`) |
| `OPERADOR` | Es uno de `+ - * / = > <` |
| `ERROR` | Cualquier otra cosa (por ejemplo `3x` o `@`) |

## Pasos

Completa [`lexico.py`](lexico.py) siguiendo los pasos y ejecútalo:

```bash
cd ejercicios/ej15-analizador-lexico
python3 lexico.py
```

## ✅ Comprueba

```text
Código: si precio > 100 entonces total = precio * 2
  RESERVADA      si
  IDENTIFICADOR  precio
  OPERADOR       >
  NUMERO         100
  RESERVADA      entonces
  IDENTIFICADOR  total
  OPERADOR       =
  IDENTIFICADOR  precio
  OPERADOR       *
  NUMERO         2
Tokens: 10 · Errores léxicos: 0

Código: mostrar 3x @ nota
  RESERVADA      mostrar
  ERROR          3x
  ERROR          @
  IDENTIFICADOR  nota
Tokens: 4 · Errores léxicos: 2
```

## ⭐ Reto (opcional)

Añade el tipo `TEXTO` para tokens entre comillas, como `"hola"`, y el operador `==`.
