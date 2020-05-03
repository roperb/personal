#Project Euler Problem 25
#1000 digit Fibonacci Number

def fibonacci(n):
    a = 1
    b = 1
    index = 2
    digits = 0
    while digits<n:
        digits = 0
        b,a = a+b,b
        c = b
        while c != 0:
            c //= 10
            digits += 1
        index+=1
    return index

print(fibonacci(1000))