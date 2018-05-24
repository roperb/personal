#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')
from genPrime import genPrime
primeList = genPrime(2000000,1)
multResult = 0
print("done first step")
for prime in primeList:
    multResult += prime

print(multResult)
