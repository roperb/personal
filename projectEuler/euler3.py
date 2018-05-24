#Project Euler Problem 3
#
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')

from primeFactor import primeFactorList

n = 600851475143
print(primeFactorList(n)[-1])
