### Suma de números (CLI)

### 1. Descripción del problema
Se desea desarrollar un programa de línea de comandos que reciba una lista de números y calcule su suma.

### 2. Objetivo del software
Ejecutar el programa con `-n`/`--numbers` y devolver la suma total.

### 3. Requisitos funcionales
- RF1: Aceptar una lista de números por CLI: `-n 1 2 3`.
- RF2: Aceptar números enteros o flotantes (decimal).
- RF3: Imprimir la suma como salida estándar.
- RF4: Si hay entradas inválidas (letras u otros valores), mostrar un mensaje:
  “Solo se aceptan enteros y flotantes.”
- RF5: Si no se proporcionan números, mostrar ayuda y terminar con error.

### 4. Requisitos no funcionales
- RNF1: Código legible (PEP8) y con docstrings.
- RNF2: Pruebas automatizadas con pytest (incluyendo casos límite).
- RNF3: Mensajes de error claros y consistentes.

### 5. Supuestos y limitaciones
- Se aceptan solo números en formato decimal (p. ej., `-3`, `2.5`, `1e-3`).
- No se aceptan literales binarios/hexadecimales (`0b1010`, `0xFF`).
- No se aceptan valores no numéricos (p. ej., `a`, `1,2`, `NaN`, `inf`).

### 6. Análisis del problema
Entrada: lista de tokens desde CLI.
Proceso: validar tokens → convertir a float → sumar.
Salida: suma impresa.

### 7. Diseño de la solución
- `parse_numbers(tokens: list[str]) -> list[float]` valida y convierte.
- `main(argv: list[str] | None) -> int` parsea argumentos, imprime suma, maneja errores.


