fib1 = 0
fib2 = 1 
print(fib1)
print(fib2)
n = 10 
i = 0 
while i<n:
    sum = fib1 + fib2
    print(sum)
    fib1 = fib2
    fib2 = sum
    i = i + 1 