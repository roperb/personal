#A palindromic number reads the same both ways.
#Find the largest palindrome made from the product of two 3-digit numbers.

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


lowerBound = 900
upperBound = 1001

palCandidate = 0
largestPal = 0
for i in range(lowerBound,upperBound):
    for j in range(lowerBound,upperBound):
        if checkIfPalindrome(i*j) == True and i*j > largestPal:
            largestPal = i*j

print(largestPal)
