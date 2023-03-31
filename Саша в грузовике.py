km/h = input("Введите пробег(трехзначное число): ")
days = input("Введите номер текущего дня: ")
s = int(km/h[0]) + int(km/h[1]) + int(km/h[2])
if s > int(days):
    print("Сброс")
else:
    print("Сегодня не сломался")