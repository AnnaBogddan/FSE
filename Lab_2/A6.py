N = int(input("Введите число прошедших секунд"))

hour = N // 3600
remains = N % 3600
minutes = remains // 60
seconds = remains % 60

print('{}:{:02}:{:02}'.format(hour, minutes, seconds))