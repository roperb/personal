#Project Euler Problem 39
"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
maxp = 0
nsolmax = 0
def commonfactors(n,m):
    factors = []
    if n > m:
        n, m = m, n
    for i in range(1,m//2+1):
        if m%i == 0 and n%i == 0:
            factors.append(i)
    return factors
for p in range(1,1001):
    nsol = 0
    for n in range(1,100):
        for m in range(n+1,100):
            if commonfactors(n,m) != [1]:
                break
            for k in range(1,100):
                c = k*(n**2+m**2)
                b = k*(2*m*n)
                a = k*(m**2-n**2)
                if a+b+c == p:
                    nsol += 1
                    break
                if a+b+c > p:
                    break
    if nsol > nsolmax:
        maxp = p
        nsolmax = nsol

print(maxp)