#Project Euler Problem 1

totalSum = 0
maxNumber = 1000
for number in range(maxNumber):
    if number%3==0 or number%5==0:
        totalSum = totalSum + number
        print(totalSum)
        print(number)
print(totalSum)
