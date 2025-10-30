x1 = float(input("Введите координату х первой точки"))
y1 = float(input("Введите координату у первой точки"))
x2 = float(input("Введите координату х второй точки"))
y2 = float(input("Введите координату у первой точки"))

def get_quarter(x, y):
    if x > 0 and y > 0:
        return "I"
    elif x < 0 and y > 0:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    elif x > 0 and y < 0:
        return "IV"

quarter1 = get_quarter(x1, y1)
quarter2 = get_quarter(x2, y2)

if quarter1 == quarter2:
    print("Yes,", quarter1)
else:
    print("No")
