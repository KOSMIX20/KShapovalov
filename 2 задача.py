x = int(input('Ввести 5-значное число '))
def number():
    if x > 9999 and x < 100000:
        a = x // 10000
        b = x % 10000
        c = b // 1000
        d = b % 1000
        f = d // 100
        i = d % 100
        e = i // 10
        w = i % 10
        print(e, w)
number()