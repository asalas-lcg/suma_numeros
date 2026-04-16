# 1. Leer secuencia

print("Introduce una secuencia de DNA (solo A, T, C, G):")
secuencia = input()
secuencia = secuencia.upper()

# Validar si la secuencia está vacía
if secuencia == "":
    print("Error: secuencia vacía")
    exit()

# Validar caracteres
es_valida = True
for caracter in secuencia:
    if caracter not in "ATCG":
        es_valida = False

if not es_valida:
    print("Error: caracteres inválidos")
    exit()

# Inicializar contadores
count_a = 0
count_t = 0
count_c = 0
count_g = 0

# Contar nucleótidos
for caracter in secuencia:
    if caracter == "A":
        count_a += 1
    if caracter == "T":
        count_t += 1
    if caracter == "C":
        count_c += 1
    if caracter == "G":
        count_g += 1

total = count_a + count_t + count_c + count_g

print("Nucleotide count:")
print("A:", count_a)
print("T:", count_t)
print("C:", count_c)
print("G:", count_g)
print("Total:", total)
