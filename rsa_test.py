import random
p = 5
q = 11
mod = (p-1)*(q-1)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def pubKey(p,q):
    mod = (p-1)*(q-1)
    keyList = list(range(2,mod))
    primefactors = list(set(prime_factors(mod)))
    x = 0
    while x < len(primefactors):
        for number in keyList:
            if number%primefactors[x]==0:
                keyList.remove(number)
        x=x+1
        """
    for number in keyList:
        for i in primefactors:           
            if number%i == 0:
                keyList.remove(number)
                break
        """
    k = keyList[random.randint(0,len(keyList)-1)]
    return k

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def keyGen(p,q):
    k = pubKey(p,q)

    j = modinv(k,(p-1)*(q-1))
    return [k,j]
                
"""k = pubKey(p,q)
j = modinv(k,mod)"""

print(keyGen(p,q),(p-1)*(q-1))



