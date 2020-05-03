#Project Euler Problem 34
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""
def diglist(n):
    digitlist = []
    while n > 0:
        digitlist.append(n%10)
        n //= 10
    return digitlist

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

total = 0
for num in range(3,10000000):
    dlist = diglist(num)
    sum = 0
    for d in dlist:
        sum += factorial(d)
    if sum == num:
        total += num

print(total)