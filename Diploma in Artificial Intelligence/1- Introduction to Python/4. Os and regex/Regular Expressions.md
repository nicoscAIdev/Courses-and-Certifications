# Hoja de Referencia de Expresiones Regulares en Python

## CARACTERES ESPECIALES

| Símbolo     | Significado |
|-------------|-------------|
| `^`         | Coincide con el inicio de una cadena. También antes de cada `\n`. |
| `$`         | Coincide con el final de una cadena. También antes de cada `\n`. |
| `.`         | Coincide con cualquier carácter excepto saltos de línea. |
| `\`         | Escapa caracteres especiales o denota clases. |
| `A\|B`      | Coincide con A o B. Si A coincide primero, B no se evalúa. |
| `+`         | Coincide de forma voraz 1 o más veces. |
| `*`         | Coincide de forma voraz 0 o más veces. |
| `?`         | Coincide de forma voraz 0 o 1 vez. Agregado a cuantificadores, actúa de forma no voraz. |
| `{m}`       | Coincide exactamente m veces. |
| `{m,n}`     | Coincide entre m y n veces. |
| `{m,n}?`    | Coincide al menos m veces (ignora n). |

## CLASES DE CARACTERES (SECUENCIAS ESPECIALES)

| Secuencia | Significado |
|-----------|-------------|
| `\w`      | Letras, dígitos y guion bajo (`_`). |
| `\d`      | Dígitos (`0-9`). |
| `\D`      | No dígitos. |
| `\s`      | Espacios en blanco (`\t`, `\n`, `\r`, espacio). |
| `\S`      | No espacios en blanco. |
| `\b`      | Límite de palabra. |
| `\B`      | No es límite de palabra. |
| `\A`      | Inicio absoluto de la cadena. |
| `\Z`      | Fin absoluto de la cadena. |

## CONJUNTOS (SETS)

| Notación    | Significado |
|-------------|-------------|
| `[amk]`     | Coincide con a, m o k. |
| `[a-z]`     | Letras de la a a la z. |
| `[a\-z]`    | Coincide con a, - o z. |
| `[a-]`      | Coincide con a o -. |
| `[-a]`      | Igual que `[a-]`. |
| `[a-z0-9]`  | Letras de a a z y dígitos. |
| `[(+*)]`    | Coincide con (, +, * o ). |
| `[^ab5]`    | Coincide con todo menos a, b o 5. |

## AGRUPACIONES

| Notación        | Significado |
|-----------------|-------------|
| `( )`           | Agrupa expresiones. |
| `(?...)`        | Extensión según el carácter siguiente. |
| `(?P<name>...)` | Grupo con nombre. |
| `(?aiLmsux)`    | Banderas:<br> a - ASCII<br> i - IgnoreCase<br> L - Locale<br> m - Multilínea<br> s - Incluye saltos<br> u - Unicode<br> x - Verbose |
| `(?:A)`         | Agrupación no capturante. |
| `(?#...)`       | Comentario. |
| `A(?=B)`        | Lookahead positivo. |
| `A(?!B)`        | Lookahead negativo. |
| `(?<=B)A`       | Lookbehind positivo. |
| `(?<!B)A`       | Lookbehind negativo. |
| `(?P=name)`     | Coincide con un grupo previamente nombrado. |
| `(...)\1`       | Coincide con el primer grupo capturado (se puede usar hasta `\99`). |

## FUNCIONES DE `re` EN PYTHON

| Función               | Descripción |
|-----------------------|-------------|
| `re.findall(A, B)`    | Devuelve una lista con todas las coincidencias de A en B. |
| `re.search(A, B)`     | Devuelve la primera coincidencia de A en B como objeto `match`. |
| `re.split(A, B)`      | Divide B usando A como delimitador. |
| `re.sub(A, B, C)`     | Reemplaza A por B en la cadena C. |

---

**Fuente:** [dataquest.io](https://www.dataquest.io)
