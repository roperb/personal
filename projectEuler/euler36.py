#Project Euler Problem 36
"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
def digtobin(n):
    return int(bin(n)[2:])

def ispal(number):
    if type(number) != type(""):
        number = str(number)
    palCheckVal = 1
    for i in range(len(number) // 2):
        if number[i] != number[-(i + 1)]:
            palCheckVal = 0

    if palCheckVal == 1:
        return True
    else:
        return False

def main():
    sum = 0
    for n in range(1000000):
        if n%2 !=0:
            if ispal(n) and ispal(digtobin(n)):
                sum += n
    print(sum)


if __name__== "__main__":
    main()
