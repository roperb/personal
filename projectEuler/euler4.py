#A palindromic number reads the same both ways.
#Find the largest palindrome made from the product of two 3-digit numbers.

import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')
sys.path.insert(0, '/Users/brianroper/Documents/github/genLibrary')

from checkIfPalindrome import checkIfPalindrome

lowerBound = 900
upperBound = 1001

palCandidate = 0
largestPal = 0
for i in range(lowerBound,upperBound):
    for j in range(lowerBound,upperBound):
        if checkIfPalindrome(i*j) == True and i*j > largestPal:
            largestPal = i*j

print(largestPal)
