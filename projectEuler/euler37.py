#Project Euler Problem 37
"""
The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes
that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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


def main():
    primelist = genPrime(1000000)
    list = []
    for p in primelist:
        if isPrime(int(str(p)[0]),primelist) and isPrime(int(str(p)[-1]),primelist):
            primeleft = p
            primeright = p
            while primeright > 10:
                primeright = digtonum(diglist(primeright)[:-1])
                primeleft = digtonum(diglist(primeleft)[1:])
                if not (isPrime(primeright,primelist) and isPrime(primeleft,primelist)):
                    break
            if p > 10 and primeleft < 10 and primeright < 10 and isPrime(primeleft,primelist) and isPrime(primeright,primelist):
                list.append(p)
    print(sum(list))

if __name__ == "__main__":
    main()