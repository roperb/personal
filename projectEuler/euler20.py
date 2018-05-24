"""
Find the sum of the digits in the number 100!
"""
import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')
sys.path.insert(0, '/Users/brianroper/Documents/github/genLibrary')

from factorial import factorial

number = str(factorial(100))
totalSum = 0
for i in range(len(number)):
    totalSum += int(number[i])
print(totalSum)
