
def genPrime(inputNumber,inputType=1):
    """
    Type 1 - list up to and includinginputNumber
    Type 2 - list of primes of length equal to inputNumber
    Type 3 - the nth primeList
    """
    if inputType == 1:
        if inputNumber < 2:
            return []
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

def isPrime(n,primelist=[]):
    if primelist == []:
        genPrime(int(n ** .5) + 1)
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