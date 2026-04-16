# 1. Leer secuencia
secuencia = input("Ingrese la secuencia de AND: ")

# 2. Convertir a mayúsculas
secuencia = secuencia.upper()
print("Secuencia ingresada:", secuencia)

# 3. Validar si está vacía
# 4. Validar caracteres
# 5. Contar nucleótidos
count_a = secuencia.count("A")
count_t = secuencia.count("T")
count_c = secuencia.count("C")
count_g = secuencia.count("G")
print("Número de adeninas (A):", count_a)
print("Número de timinas (T):", count_t)
print("Número de citosinas (C):", count_c)
print("Número de guaninas (G):", count_g)
# 6. Mostrar resultados
