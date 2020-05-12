#Project Euler Problem 41
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.

For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0, '/Users/roperb/PycharmProjects/personal/math/')

from permutation import permutation as perm
from ntlib import *
from primelib import *

primelist = genPrime(int(1000000000**.5)+1)
list = perm([1,2,3,4,5,6,7])

plist = []


for i in range(len(list)):
    num = digtonum(list[i])
    if isPrime(num,primelist):
        plist.append(num)

plist.sort()
print(plist[-1])
