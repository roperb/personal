#function to check if something is a palindrome

def checkIfPalindrome(number):
    number = str(number)
    palCheckVal = 1
    for i in range(len(number)/2):
        if number[i] != number[-(i+1)]:
            palCheckVal = 0

    if palCheckVal == 1:
        return True
    else:
        return False
    
