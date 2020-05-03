#Project Euler Problem 35
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
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

def diglist(n):
    digitlist = []
    while n > 0:
        digitlist.append(n%10)
        n //= 10
    return digitlist

def digtonum(list):
    """
    Takes a list of digits from lowest to highest and returns the number
    :param list: the list of digits from lowest to highest
    :return: the number made from those digits
    """
    num = 0
    for d in range(len(list)):
        num += list[d]*10**d
    return num

def hasdigits(n,list):
    dlist = diglist(n)
    for e in list:
        if e in dlist:
            return True
    return False

def gencircperm(n):
    circperms = []
    dlist = diglist(n)
    numperm = len(dlist)
    for i in range(numperm):
        templist = [0]*numperm
        for j in range(numperm):
            templist[j]=dlist[(i+j)%numperm]
        circperms.append(digtonum(templist))
    return circperms

def main():
    primelist = genPrime(1000000)
    circprimes = [2]

    for p in primelist:
        if not hasdigits(p,[0,2,4,6,8]):
            perm = gencircperm(p)
            checkprime = len(perm)
            for num in perm:
                if not isPrime(num,primelist):
                    break
                checkprime -= 1
            if checkprime == 0:
                circprimes.append(p)
    print(circprimes)
    print(len(circprimes))

if __name__ == "__main__":
    main()