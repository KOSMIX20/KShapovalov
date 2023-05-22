def zagadka1():
    a = print('Загадка №1\n Назовешь её и она исчезнет? \n На каждую загадку есть по 3 попытки!')
    answer = input('Введите ответ:')
    n = 0
    while n < 3:
        if answer == 'Тайна' or 'тайна':
            print('Правильный ответ!')
            break
        else:
            answer = input('Введите ответ:')
            print('Ответ неверный, попробуйте еще раз')
            n += 1
            continue

zagadka1()