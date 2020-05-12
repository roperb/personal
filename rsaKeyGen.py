#
#
#
#

import sys
sys.path.insert(0, '/Users/brianroper/Dropbox/03 - Code/genlib')
import random
import math
from gcd2 import gcd
from findModInverse import findModInverse

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

def rsaKeyGen(p, q):
    n = p*q
    mod = (p-1)*(q-1)
    keyList = list(range(2,mod))
    primefactors = list(set(prime_factors(mod)))
    x = 0
    while x < len(primefactors):
        for number in keyList:
            if number%primefactors[x]==0:
                keyList.remove(number)
        x = x+1
    e = keyList[random.randint(0,len(keyList)-1)]
    d = modinv(e,mod)
    
    return [e,d, p*q]

p = 5
q = 11

print rsaKeyGen(p, q)
print rsaKeyGen(p, q)
print rsaKeyGen(p, q)
print rsaKeyGen(p, q)
print rsaKeyGen(p, q)
print rsaKeyGen(p, q)
print rsaKeyGen(p, q)
print rsaKeyGen(p, q)
print rsaKeyGen(p, q)
print rsaKeyGen(p, q)

    
