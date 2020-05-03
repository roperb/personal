#Project Euler Problem 28

x = 1001
y = 1001
grid = [ [0] * (y) for _ in range(x)]

#sum of odd square numbers less than or equal to 1001x1001
sum1 = 0
n = 0
num = (2*n+1)**2
while num <= x*y:
    sum1 += num
    n += 1
    num = (2*n+1)**2

#sum of 1 more than an even square numbers less than or equal to 1001x1001
sum2 = 0
n = 1
num = 1+(2*n)**2
while num <= x*y:
    sum2 += num
    n += 1
    num = 1+(2*n)**2

#sum of 2n less than an odd square number
sum3 = 0
n = 1
num = (2*n+1)**2-2*n
while num <= x*y:
    sum3 += num
    n += 1
    num = (2 * n + 1) ** 2 - 2 * n

#sum of 2n+1 less than an even square number
sum4 = 0
n = 1
num = (2*n)**2 - (2*(n-1)+1)
while num <= x*y:
    sum4 += num
    n += 1
    num = (2*n)**2 - (2*(n-1)+1)

print(sum1+sum2+sum3+sum4)

