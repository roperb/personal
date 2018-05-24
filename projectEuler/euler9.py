#Pythagorean triplet is a set of three natural numbers, a < b < c, for which
#a**2 + b**2 = c**2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')
target = 1000
from pyTrip import pyTrip
n=1
m=1
nmax = 100
mmax = 100
while(n < nmax):
    m=n+1
    while(m < mmax):
        triple = pyTrip(n,m)
        if triple[0]+triple[1]+triple[2] == target:
            print(triple)
            print("this is the triple")
            print(triple[0]*triple[1]*triple[2])
            break
        m+=1
    n+=1
