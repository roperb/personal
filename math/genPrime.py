#generates primes based on 1 of 3 methods


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

"""
def genPrime(type,inputNumber):
    if type==1:
        primeList = [2,3]
        primeCandidate = primeList[-1]+2
        while primeCandidate <= inputNumber:
            if checkPrime(primeCandidate,primeList):
                primeList.append(primeCandidate)
            primeCandidate += 2
        return primeList

def checkPrime(primeCandidate,primeList):
    if primeCandidate < primeList[-1]:
        primeCheck = 1
        for prime in primeList:
            if prime**2 > primeCandidate:
                break
            if primeCandidate%prime == 0:
                primeCheck = 0
                break
        if primeCheck == 1:
            return True
        if primeCheck == 0:
            return False
    if primeCandidate > primeList[-1]:
        print("number given to checkPrime function larger than largest prime, generating sufficient list")
        newPrimeCandidate = primeList[-1]+2
        while newPrimeCandidate <= primeCandidate:
            if checkPrime(newPrimeCandidate,primeList):
                primeList.append(newPrimeCandidate)
            newPrimeCandidate += 2
        return checkPrime(primeCandidate,primeList)
testPrime = genPrime(1,1000)
"""
