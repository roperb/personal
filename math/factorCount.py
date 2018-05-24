def factorCount(number,primeList):
    """
    requires a complete list of primes in order to function
    """
    redNum = number
    degeneracyList = []
    for prime in primeList:
        if prime > number:
            break
        redNum = number
        degeneracy = 0
        while redNum%prime == 0:
            redNum = redNum / prime
            degeneracy += 1
        if degeneracy != 0:
            degeneracyList.append(degeneracy)
    numberOfFactors = 1
    for elements in degeneracyList:
        numberOfFactors *= elements+1
    return numberOfFactors
