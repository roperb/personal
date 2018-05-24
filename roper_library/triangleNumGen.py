#Triangle number generator

import sys
sys.path.insert(0, '/Users/brianroper/Dropbox/03 - Code/roper_library')

def triangleNumGen(n):
    if n > 0 and n == int(n):
        return n*(n+1)/2
    else:
        print "Bad input.  Input an integer"
