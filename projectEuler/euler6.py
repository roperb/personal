#Project Euler Problem 6

n = 100
sumSquared = ((n**2+n)/2)**2
squaredSum = 0

for i in range(n+1):
    squaredSum += i**2

print(sumSquared-squaredSum)
