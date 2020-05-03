#Project Euler Problem 36
"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
def digtobin(n):
    pass


def checkIfPalindrome(number):
    number = str(number)
    palCheckVal = 1
    for i in range(len(number) / 2):
        if number[i] != number[-(i + 1)]:
            palCheckVal = 0

    if palCheckVal == 1:
        return True
    else:
        return False

def main():
    pass

if __name__== "__main__":
    main()
