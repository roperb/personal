#Project Euler Problem 33
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify
it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

"""



for n1 in range(1,10):
    for n2 in range(0,10):
        for d1 in range(1,10):
            for d2 in range(0,10):
                fraction = (n1*10+n2)/(d1*10+d2)
                # Check if second digit is the same
                if n1*10+n2 != d1*10+d2 and fraction < 1:
                    if d2 == n2 and d2>0 and abs(n1/d1-fraction)<0.0001:
                        print(str(n1*10+n2)+"/"+str(d1*10+d2))
                    if d1 == n1 and d1>0 and d2>0 and abs(n2/d2-fraction)<0.0001:
                        print(str(n1 * 10 + n2) + "/" + str(d1 * 10 + d2))
                    if d2 == n1 and d2>0 and abs(n2/d1-fraction)<0.0001:
                        print(str(n1 * 10 + n2) + "/" + str(d1 * 10 + d2))
                    if d1 == n2 and d1>0 and d2>0 and abs(n1/d2-fraction)<0.0001:
                        print(str(n1 * 10 + n2) + "/" + str(d1 * 10 + d2))
