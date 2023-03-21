number = int(input())
if 99 >= number < 100:
    num1 = number // 10
    num2 = number % 10
    print('Число десятков',num1, '\nЧисло единиц',num2)
else:
    print('Invalid number')
    quit()
