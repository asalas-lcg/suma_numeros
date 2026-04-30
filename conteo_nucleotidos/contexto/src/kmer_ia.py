#!/usr/bin/env python3
"""
K-mer IA - Programa para contar nucleótidos en secuencias de DNA.
"""


def leer_secuencia() -> str:
    """Lee una secuencia de DNA desde entrada del usuario."""
    print("Introduce una secuencia de DNA (solo A, T, C, G):")
    secuencia = input()
    return secuencia.upper()


def validar_secuencia(secuencia: str) -> bool:
    """Valida que la secuencia contenga solo nucleótidos válidos."""
    if not secuencia:
        print("Error: secuencia vacía")
        return False

    for caracter in secuencia:
        if caracter not in "ATCG":
            print("Error: caracteres inválidos")
            return False
    return True


def contar_nucleotidos(secuencia: str) -> dict:
    """Cuenta los nucleótidos en la secuencia."""
    conteo = {"A": 0, "T": 0, "C": 0, "G": 0}

    for caracter in secuencia:
        if caracter in conteo:
            conteo[caracter] += 1

    return conteo


def mostrar_resultados(conteo: dict) -> None:
    """Muestra los resultados del conteo de nucleótidos."""
    total = sum(conteo.values())

    print("Nucleotide count:")
    print("A:", conteo["A"])
    print("T:", conteo["T"])
    print("C:", conteo["C"])
    print("G:", conteo["G"])
    print("Total:", total)


def main():
    """Función principal del programa."""
    secuencia = leer_secuencia()

    if not validar_secuencia(secuencia):
        return

    conteo = contar_nucleotidos(secuencia)
    mostrar_resultados(conteo)


if __name__ == "__main__":
    main()
