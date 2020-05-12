#Returns all primes up to a number n

import sys
sys.path.insert(0, '/Users/brianroper/Dropbox/03 - Code/genlib')

from genPrime import genPrime

import math
from fileToIntList import fileToIntList
from listToFile import listToFile
from os.path import exists

def genPrimeList(n,localPrimeFile='primelist.txt'):
    genPrime(n)
    primeList=fileToIntList(localPrimeFile)
    return primeList[0:n-1]
