#Project Euler Problem 22

"""
Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

def scoreletter(c):
    letterscore = {
        'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
        'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
        'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
        'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26
    }
    return letterscore[c]

def scorename(name):
    score = 0
    for c in name:
        score += scoreletter(c)
    return score

file = open("names.txt","r")
namestring = file.readline()
file.close()
namelist = ((''.join(c for c in namestring if c not in '"')).split(","))
namelist.sort()

nameposition = range(1,len(namelist)+1)
namescore = []
for name in namelist:
    namescore.append(scorename(name))

total = 0
for i in range(len(namescore)):
    total += nameposition[i]*namescore[i]

print(total)


