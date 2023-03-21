number = int(input())
if 99 > number < 100:
    num1 = number // 10
    num2 = number % 10
    print(num2,num1)
else:
    print('Неверное число')
