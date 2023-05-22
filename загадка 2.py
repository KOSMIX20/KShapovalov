def zagadka2():
    a = print('Загадка №2\n Два конца, два кольца посередине гвоздик?\n На каждую загадку есть по 3 попытки!')
    answer = input('Введите ответ:')
    n = 0
    while n < 3:
        if answer == 'Ножницы' or 'ножницы':
            print('Правильный ответ!')
            break
        else:
            answer = input('Введите ответ:')
            print('Ответ неверный, попробуйте еще раз')
            n += 1
            continue
        

zagadka2()