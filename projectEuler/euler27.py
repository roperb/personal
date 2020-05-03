#Project Euler Problem 27
"""
Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,402+40+41=40(40+1)+41 is divisible by 41,
and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered,
which produces 80 primes for the consecutive values 0≤n≤79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n2+an+b

, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

def genPrime(inputNumber,inputType=1):
    """
    Type 1 - list up to inputNumber
    Type 2 - list of primes of length equal to inputNumber
    Type 3 - the nth primeList
    """
    if inputType == 1:
        if inputNumber < 2:
            return "Not Appropriate"
        if inputNumber == 2:
            return [2]
        if inputNumber == 3:
            return [2,3]
        if inputNumber > 3:
            primeList = [2,3]
            primeCandidate = primeList[-1]+2
            while primeCandidate <= inputNumber:
                primeCheck = 1
                for prime in primeList:
                    if prime**2 > primeCandidate:
                        break
                    if primeCandidate%prime == 0:
                        primeCheck = 0
                        break
                if primeCheck == 1:
                    primeList.append(primeCandidate)
                primeCandidate += 2
            return primeList

    if inputType == 2:
        if inputNumber == 1:
            return [2]
        if inputNumber == 2:
            return [2,3]
        if inputNumber == 3:
            return [2,3]
        if inputNumber > 3:
            primeList = [2,3]
            primeCandidate = primeList[-1]+2
            while len(primeList) < inputNumber:
                primeCheck = 1
                for prime in primeList:
                    if prime**2 > primeCandidate:
                        break
                    if primeCandidate%prime == 0:
                        primeCheck = 0
                        break
                if primeCheck == 1:
                    primeList.append(primeCandidate)
                primeCandidate += 2
            return primeList
    if inputType == 3:
        return genPrime(inputNumber,2)[-1]
def isPrime(n,primelist):
    n = abs(n)
    if primelist[-1]**2 < n:
        primelist = genPrime(n)
    for prime in primelist:
        if n == 0 or n == 1:
            return False
        elif prime**2 > n:
            return True
        elif n%prime == 0:
            return False


def f(a,b,n):
    return n**2+a*n+b

def main():
    primelist = genPrime(1000000)
    blist = genPrime(1001)
    alist = list(range(-999,1000))
    max_n = 1
    for a in alist:
        for b in blist:
            n = 0
            isprime = True
            while isprime:
                isprime = isPrime(f(a,b,n),primelist)
                if isprime:
                    n += 1
            if n > max_n:
                max_n = n
                print(str(a)+" "+str(b)+" "+str(n))

if __name__ == "__main__":
    main()