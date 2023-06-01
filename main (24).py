def is_year_leap(year):
    if year % 100 == 0:
        if year %  400 == 0:
            return "Год высокосный"
        else:
            return "Год не высокосный"

    elif year % 4 == 0:
        return "Год высокосный"

    else:
        return "Год не высокосный"

x = is_year_leap(int(input('Введите год: ')))
print(x)
