def read_protein_data(filename):
    proteins = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t")
                if len(parts) >= 3:
                    protein_data = (
                        parts[0].strip(),  # name
                        parts[1].strip(),  # organism
                        parts[2].strip()  # sequence
                    )
                    proteins.append(protein_data)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    return proteins


def decode_rle_sequence(sequence):
    result = []
    i = 0
    while i < len(sequence):
        if sequence[i].isdigit():
            num_str = ""
            while i < len(sequence) and sequence[i].isdigit():
                num_str += sequence[i]
                i += 1
            if i < len(sequence):
                count = int(num_str)
                amino_acid = sequence[i]
                result.append(amino_acid * count)
                i += 1
        else:
            result.append(sequence[i])
            i += 1
    return "".join(result)


def search_operation(proteins, search_sequence, operation_num):
    results = []
    for name, organism, sequence in proteins:
        decoded_sequence = decode_rle_sequence(sequence)
        if search_sequence in decoded_sequence:
            results.append((organism, name))

    output_lines = [f"{operation_num:03d} search {search_sequence}"]
    output_lines.append("organism protein")

    if results:
        for organism, name in results:
            output_lines.append(f"{organism} {name}")
    else:
        output_lines.append("NOT FOUND")

    return output_lines


def diff_operation(proteins, protein1_name, protein2_name, operation_num):
    protein1_seq = None
    protein2_seq = None
    protein1_found = False
    protein2_found = False

    # Ищем последовательности белков
    for name, organism, sequence in proteins:
        if name == protein1_name:
            protein1_seq = decode_rle_sequence(sequence)
            protein1_found = True
        if name == protein2_name:
            protein2_seq = decode_rle_sequence(sequence)
            protein2_found = True

    output_lines = [f"{operation_num:03d} diff {protein1_name} {protein2_name}"]
    output_lines.append("amino-acids difference:")

    if not protein1_found or not protein2_found:
        missing_proteins = []
        if not protein1_found:
            missing_proteins.append(protein1_name)
        if not protein2_found:
            missing_proteins.append(protein2_name)
        output_lines.append("MISSING: " + ", ".join(missing_proteins))
    else:
        # Сравниваем последовательности
        min_len = min(len(protein1_seq), len(protein2_seq))
        differences = 0

        # Считаем различия в общей части
        for i in range(min_len):
            if protein1_seq[i] != protein2_seq[i]:
                differences += 1

        # Добавляем различия из-за разной длины
        differences += abs(len(protein1_seq) - len(protein2_seq))

        output_lines.append(str(differences))

    return output_lines


def mode_operation(proteins, protein_name, operation_num):
    protein_seq = None
    protein_found = False

    # Ищем последовательность белка
    for name, organism, sequence in proteins:
        if name == protein_name:
            protein_seq = decode_rle_sequence(sequence)
            protein_found = True
            break

    output_lines = [f"{operation_num:03d} mode {protein_name}"]
    output_lines.append("amino-acid occurs:")

    if not protein_found:
        output_lines.append(f"MISSING: {protein_name}")
    else:
        # Подсчитываем частоту аминокислот
        counts = {}
        for amino_acid in protein_seq:
            counts[amino_acid] = counts.get(amino_acid, 0) + 1

        # Находим максимальную частоту
        max_count = 0
        for count in counts.values():
            if count > max_count:
                max_count = count

        # Находим аминокислоты с максимальной частотой
        max_amino_acids = [aa for aa, count in counts.items() if count == max_count]

        # Сортируем по алфавиту и берем первую
        max_amino_acids.sort()
        most_common = max_amino_acids[0]

        output_lines.append(f"{most_common} {max_count}")

    return output_lines

def main():
    proteins = read_protein_data("sequences.1.txt")

    try:
        with open("commands.1.txt", "r", encoding="utf-8") as cmd_file:
            commands = cmd_file.readlines()
    except FileNotFoundError:
        print("Файл commands.txt не найден")
        return

    # Подготавливаем выходной файл
    output_lines = ["Ivan Ivanov", "Genetic Searching"]

    # Обрабатываем команды
    for i, command in enumerate(commands, 1):
        command = command.strip()
        if not command:
            continue

        parts = command.split("\t")
        operation = parts[0].strip()

        # Добавляем разделитель после второй строки вывода
        if i == 1:
            output_lines.append("-" * 50)
        else:
            # Для остальных операций добавляем разделители
            output_lines.append("-" * 50)

        if operation == "search":
            if len(parts) >= 2:
                search_seq = parts[1].strip()
                result = search_operation(proteins, search_seq, i)
                output_lines.extend(result)

        elif operation == "diff":
            if len(parts) >= 3:
                protein1 = parts[1].strip()
                protein2 = parts[2].strip()
                result = diff_operation(proteins, protein1, protein2, i)
                output_lines.extend(result)

        elif operation == "mode":
            if len(parts) >= 2:
                protein_name = parts[1].strip()
                result = mode_operation(proteins, protein_name, i)
                output_lines.extend(result)

    with open("genedata.1.txt", "w", encoding="utf-8") as output_file:
        for line in output_lines:
            output_file.write(line + "\n")

    print("Результаты записаны в файл genedata.txt")

if __name__ == "__main__":
    main()

