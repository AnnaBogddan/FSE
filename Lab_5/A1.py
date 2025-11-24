text = str(input("Введите строку "))
while "(" in text:
    left = text.rfind("(")
    right = text.find(")", left)
    if right == -1:
        break

    text = text[:left] + text[right+1:]

print(text)