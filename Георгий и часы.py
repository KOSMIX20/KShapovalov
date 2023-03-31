hours = input("Введите отработанные часы: ")
ost = input("Введите остаток по крелиту: ")
foods = input("Введите траты на еду: ")
t = float(ost) + float(foods)
z = ((200 * float(hours))/2**3) + float(hours)
if z >= t:
    print("Часов хватает")
else:
    print("Часов не хватает!")
