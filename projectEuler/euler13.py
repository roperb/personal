import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')
sys.path.insert(0, '/Users/brianroper/Documents/github/genLibrary')

from fileToIntList import fileToIntList

fileList = fileToIntList('euler13.txt')
totalSum = 0
for number in fileList:
    totalSum += number

print(totalSum)
