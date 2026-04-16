"""
CLI para sumar números proporcionados por línea de comandos.

Acepta números enteros o flotantes en formato decimal y muestra la suma total.
"""

from __future__ import annotations

import argparse
import math
import sys
from typing import List


ERROR_MESSAGE = "Solo se aceptan enteros y flotantes."


def parse_numbers(tokens: List[str]) -> List[float]:
    """
    Valida y convierte una lista de tokens en números flotantes.

    Parámetros
    ----------
    tokens : list[str]
        Lista de valores proporcionados por la línea de comandos.

    Retorna
    -------
    list[float]
        Lista de números convertidos a float.

    Lanza
    -----
    ValueError
        Si algún token no es un número decimal válido o representa NaN/inf.
    """
    numbers: List[float] = []

    for token in tokens:
        try:
            value = float(token)
        except ValueError as exc:
            raise ValueError(ERROR_MESSAGE) from exc

        # Rechazar NaN e infinitos explícitamente
        if math.isnan(value) or math.isinf(value):
            raise ValueError(ERROR_MESSAGE)

        numbers.append(value)

    return numbers


def build_parser() -> argparse.ArgumentParser:
    """
    Construye y configura el parser de argumentos.

    Retorna
    -------
    argparse.ArgumentParser
        Parser configurado para el CLI.
    """
    parser = argparse.ArgumentParser(
        description="Suma una lista de números proporcionados por línea de comandos."
    )

    parser.add_argument(
        "-n",
        "--numbers",
        nargs="+",
        required=True,
        help="Lista de números a sumar (enteros o flotantes).",
    )

    return parser


def main(argv: List[str] | None = None) -> int:
    """
    Punto de entrada principal del programa.

    Parámetros
    ----------
    argv : list[str] | None
        Lista de argumentos (sin el nombre del programa). Si es None,
        se usan los argumentos de sys.argv.

    Retorna
    -------
    int
        Código de salida del programa:
        0 si la ejecución fue exitosa,
        distinto de 0 si ocurrió un error.
    """
    parser = build_parser()

    try:
        args = parser.parse_args(argv)
        numbers = parse_numbers(args.numbers)
        result = sum(numbers)
        print(result)
        return 0

    except ValueError as err:
        print(err, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())


