#Project Euler Problem 5

import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')

from factorList import factorList

n = 20*19*17*13*11*7*3

while factorList(n,range(1,21)) != range(1,21):
    n += 20*19*17*13*11*7*3
print(n)
