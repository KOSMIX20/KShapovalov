x = int(input('Ввести 3-значное число '))
def number():
    if x > 99 and x < 1000:
        a = x // 100
        b = x % 100
        c = b // 10
        d = b % 10
        r = d - c - a 
        print(r)
number()