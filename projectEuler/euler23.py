#Project Euler Problem 23
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def genFactorList(n):
    factorList = [1]
    for num in range(2,int(n**.5)+1):
        if n%num == 0:
            if num**2 != n:
                factorList.append(num)
                factorList.append(int(n/num))
            else:
                factorList.append(num)
    return factorList

def isAbundantNum(n):
    factorlist = genFactorList(n)
    if sum(factorlist) > n:
        return True
    return False

def genAbundantNumList(n=28130):
    abundantnumlist = []
    for num in range(1,n+1):
        if isAbundantNum(num):
            abundantnumlist.append(num)
    return abundantnumlist



def main():
    pass
    n = 28123
    alist = genAbundantNumList()

    i = 0
    sumalist = []
    while alist[i]<n+1:
        j = i
        tempsum = alist[i]+alist[j]
        while tempsum < n+1:
            #if tempsum not in sumalist:
            sumalist.append(tempsum)
            j+=1
            tempsum = alist[i] + alist[j]
        i+=1
        if i == len(alist):
            break

    notalist=[]
    for i in range(28124):
        notalist.append(i)

    z = len(sumalist)
    sumalist.sort()

    sumalist = list(dict.fromkeys(sumalist))



    for num in sumalist:
        notalist[num] = 0

    print(sum(notalist))


if __name__ == "__main__":
    main()

