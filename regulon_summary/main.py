# Programa regulon_summary que por cada TF obtiene
# TF Total de genes regulados Lista de genes
# AraC 2 araA, araB

# Algoritmo:
# 1. Leer el archivo de texto y almacenar su contenido en una variable.
# 2. Crear una estructura para akmacenar la información de cada TF.
# 3. Leer la información de ese TF

interactions = [
    ('AraC', 'araA', '+'),
    ('AraC', 'araB', '-'),
    ('LacI', 'lacZ', '-'),
    ('CRP', 'lacZ', '+'),
    ('CRP', 'araA', '+')
]

# creamos la estructura para almacenar la información de cada TF, en este caso un diccionario donde la clave es el nombre del TF y el valor es una lista de genes regulados por ese TF. Por ejemplo:
# "AraC" --> ["aracC", "araB"]

"AraC"--> "genes" --> ["araA", "araB"]
"AraC" --> "activados" --> 1
"AraC" --> "reprimidos" --> 1

regulon = {} # diccionario con lista de genes
for tf, gene, effect in interactions:
    if tf not in regulon:
        regulon[tf] = {"genes":[],
                          "activados":0,
                          "reprimidos":0
        }
    regulon[tf]["genes"].append(gene)
    


# imprimirmos el resumen de cada TF
print("TF\tTotal de genes regulados\tLista de genes")

for tf in sorted(regulon):
    total_genes = len(regulon[tf]["genes"])
    lista_genes = ", ".join(regulon[tf]["genes"])
    print(f"{tf}\t{total_genes}\t{lista_genes}")
    



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

print(interactions)