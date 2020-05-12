#Project Euler Problem 40
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

c = ""
i = 0
while len(c) < 10000002:
    c += str(i)
    i += 1
print(int(c[1])*int(c[10])*int(c[100])*int(c[1000])*int(c[10000])*int(c[100000])*int(c[1000000]))
