def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            print(ch, end='')
        print()

def draw_right_triangle(rows, ch):
    for i in range(rows):
        for j in range(i + 1):
            print(ch, end='')
        print()

def draw_frame(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end='')
            else:
                print(' ', end='')
        print()


if __name__ == "__main__":
    n = int(input("Введите количество строк (n): "))
    m = int(input("Введите количество столбцов (m): "))
    symbol = input("Введите символ для отрисовки: ")

    print(f"\n1. Прямоугольник: {n}*{m}")
    draw_rectangle(n, m, symbol)

    print("\n2. Правый треугольник:")
    draw_right_triangle(n, symbol)

    print(f"\n3. Рамка: {n}*{m}")
    draw_frame(n, m, symbol)