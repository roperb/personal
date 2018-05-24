#Project Euler Problem 8
#Find the largest product of adjacent 13 numbers in the 1000 digit number

import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')
sys.path.insert(0, '/Users/brianroper/Documents/github/genLibrary')

from fileToIntList import fileToIntList

fileList = fileToIntList('euler8.txt')

fileListStripped = []
for i in fileList:
    i = str(i)
    for j in i:
        fileListStripped.append(int(j))

product = 0
i = 0
nMult = 13
while i < len(fileListStripped)-nMult-1:
    testProduct = 1
    j = 0
    while j < nMult:
        testProduct *= fileListStripped[i+j]
        j+=1
    if testProduct > product:
        product = testProduct
    i+=1

    #testProduct = fileListStripped[i]*fileListStripped[i+1]*fileListStripped[i+2]*fileListStripped[i+3]*fileListStripped[i+4]

print(product)
