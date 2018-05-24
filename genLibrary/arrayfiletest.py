import math
from listToFile import listToFile
from fileToIntList import fileToIntList
from os.path import exists

a = [[1,2,3],[4,5,6]]
print(a)
listToFile(a,'testlist.txt')

b = fileToIntList('testlist.txt')

print(b)
print(b[1])
