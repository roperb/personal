

import sys
sys.path.insert(0, '/Users/brianroper/Documents/github/math')

def factorList(number,masterFactorList):
    factorList = []
    for factor in masterFactorList:
        if number % factor == 0:
            factorList.append(factor)

    return factorList
