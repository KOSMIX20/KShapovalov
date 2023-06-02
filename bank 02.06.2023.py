def bank(a,time):
    for each_year in range(time):
        a = (a * 1.1)
    return a

a=int(input("Vpishite money "))
time=int(input("Skolko let "))

print(bank(a, time))