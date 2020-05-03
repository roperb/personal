#Project Euler Problem 31
"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
p1 = 1
p2 = 2
p5 = 5
p10 = 10
p20 = 20
p100 = 100
p200 = 200
"""
total = 2000
count = 0
for a1 in range(total//p1):
    for a2 in range(total//p2):
        for a5 in range(total//p5):
            for a10 in range(total//p10):
                for a20 in range(total//p20):
                    for a100 in range(total//p100):
                        for a200 in range(total//p200):
                            if a1*p1+a2*p2+a5*p5+a10*p10+a20*p20+a100*p100+a200*p200 == total:
                                count += 1
print(count)
"""