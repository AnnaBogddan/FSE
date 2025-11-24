text = str(input("Введите строку "))

world = text.split()

for i in world:
    if len(i) >= 3:
        print(i[0].upper(), end='')