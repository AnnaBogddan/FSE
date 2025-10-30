prev = int(input("Введите предыдущее показание счетчика"))
curr = int(input("Введите текущее показание счетчика"))

if curr >= prev:
    used = curr - prev
else:
    used = 10000 - prev + curr

if used <= 300:
    payment = 21
elif used <= 600:
    payment = 21 + (used - 300) * 0.06
elif used <= 800:
    payment = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    payment = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025


avg_price = payment / used


print(f"Предыдущее Текущее Использовано К оплате Ср. цена m^3")
print(f"{prev:7} {curr:8} {used:10} {payment:11.2f} {avg_price:10.2f}")