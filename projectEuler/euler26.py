#Project Euler Problem 26
"""
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains
the longest recurring cycle in its decimal fraction part.
"""


def gendeclist(d,n):
    """
    writes the decimal expansion of 1/d to a list with length n
    :param d: denominator of a unit fraction
    :param n: length of output list
    :return: list of decimal expansion
    """
    declist = []
    if d == 1:
        return [0]
    decimalnum = countdec(d)

    for i in range(decimalnum-1):
        declist.append(0)

    numerator = 10**decimalnum
    divisor = d
    for i in range(n-len(declist)):

        quotient = numerator // divisor
        remainder = numerator % divisor
        declist.append(quotient)
        #next numerator is remainder *10?
        numerator = remainder*10
    return declist
def gendecstring(d,n):
    declist = ''
    if d == 1:
        return '0'
    decimalnum = countdec(d)

    for i in range(decimalnum - 1):
        declist+='0'

    numerator = 10 ** decimalnum
    divisor = d
    for i in range(n - len(declist)):
        quotient = numerator // divisor
        remainder = numerator % divisor
        declist+=str(quotient)
        # next numerator is remainder *10?
        numerator = remainder * 10
    return declist
def countdec(n):
    """
    counts the number of digits, base 10, for the number n
    :param n: input number
    :return: number of decimals base 10
    """
    n = int(abs(n))
    d = 0
    while n != 0:
        n = n // 10
        d += 1
    return d
def finddecpattern(declist):
    firstdigitpos = 0
    #patternlength = 1
    ##find the first nonzero
    while declist[firstdigitpos] == 0:
        firstdigitpos += 1
    p = firstdigitpos
    print(p)
    #pl = patternlength
    n = 0
    while p < 1000:
        n = 0
        pl = 1
        while pl<1000:
            if declist[p+pl*n:(p+pl*(n+1))] != declist[p+pl*(n+1):(p+pl*(n+2))]:
                pl += 1
            else:
                n = n+1
            if n == 20:
                return ("position = "+str(p)+" pattern length = "+str(pl))
        p = p+1
def main():


    for num in range(2,1000):
        declist=gendeclist(num,1000001)
        print("number "+str(num)+" "+finddecpattern(declist))
    #declist = gendeclist(2,1000001)
    #print(finddecpattern(declist))




if __name__ == "__main__":
    main()
