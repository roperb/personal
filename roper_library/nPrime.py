#Generates the nth prime

import sys
sys.path.insert(0, '/Users/brianroper/Dropbox/03 - Code/roper_library')

from genPrime import genPrime

import math
from fileToIntList import fileToIntList
from listToFile import listToFile
from os.path import exists

def nPrime(n, localPrimeFile='primelist.txt'):
    if exists(localPrimeFile):
        print "Local file containing list of primes exists called ",localPrimeFile
        primeList=fileToIntList(localPrimeFile)
        if len(primeList) > n:
            return primeList[0:n-1]
        else:
            while n > len(primeList):
                newPrime = primeList[-1]
                notPrime = 1
                while notPrime == 1:
                    newPrime += 2
                    notPrime = 0
                    for prime in primeList:
                        if prime**2 > newPrime:
                            break
                        if newPrime%prime == 0:
                            notPrime = 1
                            break
                primeList.append(newPrime)
        listToFile(primeList, 'primelist.txt')
        return primeList[n-1]
    else:
        genPrime(10)
        nPrime(n)

nPrime(100000)
