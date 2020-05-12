#Prime Factor List Generator

import sys
sys.path.insert(0, '/Users/brianroper/Dropbox/03 - Code/genlib')
from genPrimeList import genPrimeList

import math
from fileToIntList import fileToIntList
from listToFile import listToFile
from os.path import exists

def primeFactors(n,mode="full",localPrimeFile='primelist5.txt'):
    primeList=fileToIntList(localPrimeFile)
    if mode == "full":
        primeFactorList = []
        while n != 1:
            primeLimitCheck = 0
            for prime in primeList:
                if n == 1:
                    break
                if n%prime == 0:
                    n = n/prime
                    primeFactorList.append(prime)
                    break
                if prime == primeList[-1] and n != 1:
                    primeLimitCheck = 1
            if primeLimitCheck == 1:
                print "not enough primes!  Get a bigger prime list!"
                quit()

    if mode == "short":
        primeFactorList = []
        while n != 1:
            primeLimitCheck = 0
            for prime in primeList:
                if n == 1:
                    break
                if n%prime == 0:
                    n = n/prime
                    if len(primeFactorList) > 0:
                        if prime != primeFactorList[-1]:
                            primeFactorList.append(prime)
                    break
                if prime == primeList[-1] and n != 1:
                    primeLimitCheck = 1
            if primeLimitCheck == 1:
                print "not enough primes!  Get a bigger prime list!"
                quit()

    return primeFactorList

#Short doesn't work
