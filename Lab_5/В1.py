def read_protein_data(filename):
    proteins = []
    file = open(filename, "r", encoding="utf-8")
    for line in file:
        line = line.strip()
        parts = line.split("\t")
        # Сохраняем данные как кортеж
        protein_data = (
            parts[0].strip(),  # name
            parts[1].strip(),  # organism
            parts[2].strip()  # sequence
        )
        proteins.append(protein_data)
    return proteins

filename = "sequences.0.txt"
# Читаем данные из файла
proteins = read_protein_data(filename)

for i, protein in enumerate(proteins, 1):
    name, organism, sequence = protein  # распаковка кортежа
    print(f"Белок {i}:")
    print(f"   Название: {name}")
    print(f"   Организм: {organism}")
    print(f"   АминокислотыЖ {sequence}")
