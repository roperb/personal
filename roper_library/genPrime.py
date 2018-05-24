#Generates all primes up to a number n using an initial list

import sys
sys.path.insert(0, '/Users/brianroper/Dropbox/03 - Code/roper_library')
sys.path.insert(0, 'C:\Users\Brian/Dropbox/03 - Code/roper_library')

import math
from fileToIntList import fileToIntList
from listToFile import listToFile
from os.path import exists

def genPrime(n,localPrimeFile='primelist.txt'):
    if exists(localPrimeFile):
        print("Local file containing list of primes exists called",localPrimeFile)
        primeList=fileToIntList(localPrimeFile)
        newPrime = primeList[-1]
        
        while n > primeList[-1]:
            newPrime += 2
            notPrime = 0
            for prime in primeList:
                if newPrime%prime == 0:
                    notPrime=1
                    break
                if prime**2 > newPrime:
                    break
            if notPrime == 0:
                primeList.append(newPrime)
                
        listToFile(primeList, 'primelist.txt')
        
        
    else:
        print("Local file containing list of primes doesn't exist.  Makng one")
        primeList = [2,3]
        listToFile(primeList, 'primelist.txt')
        genPrime(n)

genPrime(100000)
