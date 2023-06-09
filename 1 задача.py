x = int(input('Ввести 4-значное число '))
def number():
    if x > 999 and x < 10000:
        a = x // 1000
        b = x % 1000
        c = b // 100
        d = b % 100
        f = d // 10
        i = f % 10    
        s = a + c + f + i
        g = a * c * f * i
        print(s, g)
number()