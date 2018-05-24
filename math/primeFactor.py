#prime factor generator

import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')

from genPrime import genPrime

def primeFactorList(n,factorType=1):
    """
    factorType 1 - list without repeats
    factorType 2 - list with repeats
    """
    primeFactorList=[]
    maxPrime = int(n**.5)+1
    primeList = genPrime(maxPrime,1)
    if factorType == 1:
        for prime in primeList:
            if n % prime == 0:
                primeFactorList.append(prime)
    if factorType == 2:
        while n > 1:
            for prime in primeList:
                if n % prime == 0:
                    primeFactorList.append(prime)
                    n /= prime
                    n = int(n)
                    break
                if n == 1:
                    break

    return primeFactorList
