#Project Euler Problem 42
"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.

For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.

If the word value is a triangle number then we shall call the word a triangle word.

How many triangle words are there?
"""
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0, '/Users/roperb/PycharmProjects/personal/math/')
sys.path.insert(0, '/Users/roperb/PycharmProjects/personal/genlib/')

from ftolist import csvtolist
import scrabblelib
list = csvtolist("words.txt")
trilist = []
for i in range(1,30):
    trilist.append(int(0.5*i*(i+1)))
scorelist = []
for word in list:
    scorelist.append(scrabblelib.scoreword(word))
print(scorelist)
print(trilist)
numtri = 0
for num in scorelist:
    if num in trilist:
        numtri += 1
print(numtri)
