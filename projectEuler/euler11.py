#What is the greatest product of four adjacent numbers in the same direction
#(up, down, left, right, or diagonally) in the 20x20 grid?

import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')
sys.path.insert(0, '/Users/brianroper/Documents/github/genLibrary')

from fileToIntList import fileToList

fileList = fileToList('euler11.txt')

print(fileList)
print(len(fileList))
print(len(fileList[0]))

def largestInList(inputList):
    largest = 0
    for number in inputList:
        if number > largest:
            largest = number
    return largest

def multRight(inputList):
    largest = 0
    for row in inputList:
        i = 0
        while i < len(row)-3:
            if row[i]*row[i+1]*row[i+2]*row[i+3] > largest:
                largest = row[i]*row[i+1]*row[i+2]*row[i+3]
            i+=1
    return largest

def multDown(inputList):
    largest = 0
    i = 0
    while i < len(inputList[0])-3:
        j = 0
        while j < len(inputList):
            a,b,c,d = inputList[i][j],inputList[i+1][j],inputList[i+2][j],inputList[i+3][j]
            if largest < a*b*c*d:
                largest = a*b*c*d
            j+=1
        i+=1
    return largest

def multDiagRight(inputList):
    largest = 0
    i = 0
    while i < len(inputList[0])-3:
        j = 0
        while j < len(inputList)-3:
            a,b,c,d = inputList[i][j],inputList[i+1][j+1],inputList[i+2][j+2],inputList[i+3][j+3]
            if largest < a*b*c*d:
                largest = a*b*c*d
            j+=1
        i+=1
    return largest
def multDiagLeft(inputList):
    largest = 0
    i = 0
    while i < len(inputList[0])-3:
        j = 0
        while j < len(inputList)-3:
            a,b,c,d = inputList[i][j+3],inputList[i+1][j+2],inputList[i+2][j+1],inputList[i+3][j]
            if largest < a*b*c*d:
                largest = a*b*c*d
            j+=1
        i+=1
    return largest

print(multRight(fileList))
print(multDown(fileList))
print(multDiagRight(fileList))
print(multDiagLeft(fileList))
