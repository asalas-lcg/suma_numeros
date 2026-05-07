# =========================================
# Lectura del archivo y construcción de interactions
# =========================================

interactions = []

filename = "data/raw/NetworkRegulatorGene.tsv"

if not os.path.exists(filename):
    print("Error: archivo no encontrado")
    exit(1)
else:
    with open(filename) as f:

        for line in f:

            line = line.strip()

            print(f"Leído: {line[:50]}...")

            # Ignorar líneas vacías
            if not line:
                continue

            # Ignorar comentarios
            if line.startswith("#"):
                continue

            # Ignorar encabezado
            if line.startswith("1)regulatorId"):
                continue

            fields = line.split("\t")

            # Validar número mínimo de columnas
            if len(fields) <= 6:
                continue

            # columnas a utilizar
            TF = fields[1]
            gene = fields[3]
            effect = fields[5]

            # Validar effect
            if effect not in ["+", "-"]:
                continue

            interactions.append((TF, gene, effect))

print(interactions[:5])

# Construcción del regulon con informacion extra

regulon = {}  # diccionario con lista de genes
for tf, gene, effect in interactions:
    if tf not in regulon:
        regulon[tf] = {"genes": [], "activados": 0, "reprimidos": 0}
    regulon[tf]["genes"].append(gene)

# Contar activados y reprimidos
if effect == "+":
    regulon[tf]["activados"] += 1
elif effect == "-":
    regulon[tf]["reprimidos"] += 1
elif effect == "+-":
    regulon[tf]["activados"] += 1
    regulon[tf]["reprimidos"] += 1

# AraC {
#     "genes": ["gene1", "gene2", ...],"genes": [araC, araA, araB, araD],
#     "activados": 0,
#    "reprimidos": 0
#  }

# imprimimos el resumen de cada TF
print("TF\tTotal de genes regulados\tLista de genes")

for tf in sorted(regulon):
    total_genes = len(regulon[tf]["genes"])
    lista_genes = ",".join(regulon[tf]["genes"])
    print(f"{tf}\t{total_genes}\t{lista_genes}")
