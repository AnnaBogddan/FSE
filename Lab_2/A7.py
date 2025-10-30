x1 = int(input("Введите координату х первой клетки"))
y1 = int(input("Введите координату y второй клетки"))
x2 = int(input("Введите координату х первой клетки"))
y2 = int(input("Введите координату y второй клетки"))

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
    if (x1 + y1) % 2 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")