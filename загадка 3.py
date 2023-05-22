def zagadka3():
    a = print('Загадка №3\n Зимой и летом одним цветом, что это?\n На каждую загадку есть по 3 попытки!')
    answer = input('Введите ответ:')
    n = 0
    while n < 3:
        if answer == 'Ёлка' or 'ёлка' or 'Елка' or 'елка':
            print('Правильный ответ!')
            break
        else:
            answer = input('Введите ответ:')
            print('Ответ неверный, попробуйте еще раз')
            n += 1
            continue
zagadka3()