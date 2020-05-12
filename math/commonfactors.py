def commonfactors(n,m):
    factors = []
    if n > m:
        n, m = m, n
    for i in range(1,m//2+1):
        if m%i == 0 and n%i == 0:
            factors.append(i)
    return factors