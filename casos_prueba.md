# Casos de prueba — Suma de números (CLI)

## Caso 1: Enteros normales
- Entrada: `-n 1 2 3 4`
- Esperado: imprime `10.0` y exit code 0.

## Caso 2: Flotantes normales
- Entrada: `-n 0.5 1.25`
- Esperado: imprime `1.75` y exit code 0.

## Caso 3: Caso límite — un solo número
- Entrada: `-n 5`
- Esperado: imprime `5.0` y exit code 0.

## Caso 4: Caso límite — negativos
- Entrada: `-n 5 -2 -3`
- Esperado: imprime `0.0` y exit code 0.

## Caso 5: Caso límite — notación científica (decimal)
- Entrada: `-n 1e-3 2e-3`
- Esperado: imprime `0.003` y exit code 0.

## Caso 6: Inválido — letra
- Entrada: `-n 1 a 3`
- Esperado: mensaje “Solo se aceptan enteros y flotantes.” y exit code distinto de 0.

## Caso 7: Inválido — hexadecimal
- Entrada: `-n 0x10 2`
- Esperado: mensaje “Solo se aceptan enteros y flotantes.” y exit code distinto de 0.

## Caso 8: Inválido — NaN/inf
- Entrada: `-n NaN 2` o `-n inf 2`
- Esperado: mensaje “Solo se aceptan enteros y flotantes.” y exit code distinto de 0.

## Caso 9: Inválido — falta `-n`
- Entrada: *(sin argumentos)*
- Esperado: ayuda de argparse y exit code distinto de 0.


