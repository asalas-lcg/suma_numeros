# 1. Leer secuencia
dna_sequence = input("Ingrese la secuencia de ADN (A,T,G,C,N): ").strip

# 2. Covertir a mayúsculas
dna_sequence = dna_sequence.upper()

# 3. Leer 'k'
k = input("Ingrese el valor de k: ").strip()

# 4. Convertir 'k' a entero
k = int(k)

# 5. Validar secuencia
# Si dna_sequence esta vacía, entonces
if not dna_sequence:
    print("La secuencia DNA no puede estar vacía.")
    exit()
# Si dna_sequence contiene caracteres no válidos, entonces
valid_nucleotides = set("ATGCN")
for n in dna_sequence:
    if n not in valid_nucleotides:
        print(f"Error: el carácter '{n}' no es válido en la secuencia DNA.")
        exit()

# 6. Validar 'k'
# k tiene que ser un entero positivo y menor o igual a la longitud de dna_sequence

if k <= 0:
    print("Error: el valor de k no es válido.")
    exit()

if k > len(dna_sequence):
    print("Error: el valor de k excede la longitud de la secuencia.")
    exit()

# 7. Generar k-mers
for i in range(len(dna_sequence) - k + 1):
    kmer = dna_sequence[i : i + k]
    print(kmer)

# 8. Mostrar resultados
print("Los k-mers generados son:")
