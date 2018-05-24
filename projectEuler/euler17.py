"""
If the numbers 1 to 5 are written out in words:

one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

specialDigit = [3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,9,8,6] #last is twenty
tensDigit = [6,6,5,5,5,7,6,6] #twenty through ninety
hundredsDigit = [10,10,12,11,11,10,12,12,11]

def digitCounter(n):
    specialDigit = [3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8,6] #last is twenty
    tensDigit = [6,6,5,5,5,7,6,6] #twenty through ninety
    hundredsDigit = [10,10,12,11,11,10,12,12,11]
    if n < 21:
        return specialDigit[n-1]
    if n > 20 and n%10 == 0 and n < 100:
        return tensDigit[n/10 - 2]
    if n > 20 and n%10 != 0 and n < 100:
        return tensDigit[(n-n%10)/10 - 2] + specialDigit[n%10-1]
    if n < 1000 and n%100 == 0:
        return hundredsDigit[n/100-1]
    if n < 1000 and n%100 != 0:
        addDigit = hundredsDigit[(n-n%100)/100-1]+3
        n = n%100
        if n < 21:
            return specialDigit[n-1]+addDigit
        if n > 20 and n%10 == 0 and n < 100:
            return tensDigit[n/10 - 2]+addDigit
        if n > 20 and n%10 != 0 and n < 100:
            return tensDigit[(n-n%10)/10 - 2] + specialDigit[n%10-1]+addDigit
    if n == 1000:
        return 11

digitSum = 0
for number in range(1,1001):
    digitSum+=digitCounter(number)
print(digitSum)
