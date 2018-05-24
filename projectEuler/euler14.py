"""
The following iterative sequence is defined for the set of positive integers:

n = n/2 (n is even)
n = 3n + 1 (n is odd)


It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')
sys.path.insert(0, '/Users/brianroper/Documents/github/genLibrary')

from collatz import collatzStepNumber

largestStep = 0
largestCollatzNumber = 0
for n in range(1000001):
    collatzSteps = collatzStepNumber(n)
    if collatzSteps > largestStep:
        largestStep = collatzSteps
        largestCollatzNumber = n
print(largestCollatzNumber)
print(largestStep)
