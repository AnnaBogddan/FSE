import re

a = input("Введите предлежения ").strip()

text = re.split(r'(?<=[.?!]) ', a)

for a in text:
    print(a.strip())

print(f"Предложений в тексте {len(text)}")
