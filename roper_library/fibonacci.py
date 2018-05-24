#Fibonacci generator
#Generates the sequence of Fibonacci numbers to the nth term or below a number k

#Usage
#
#If method = "ntermlist" then the sequence will return a list of the sequence to the nth term
#If method = "nterm" then the sequence will return the nth term
#If method = "max" then it returns a sequence as a list below given number "n".
#The terms are numbered assuming the sequence beguns [0,1,1,2,3,5...]


def fibonacci(n,method="ntermlist"):
    fib_list = [0,1]
    if method == "ntermlist":
        if n == 1 or n == 2:
            return fib_list[n-1]
        else:
            i = 3
            while i<=n:
                fib_list.append(fib_list[-1]+fib_list[-2])
                i+=1

    if method == "nterm":
        a = 0
        b = 1
        i = 3
        while i <=n :
            i+=1
            a,b = b,a+b

        fib_list = b
        if n == 1:
            fib_list = a
        if n == 2:
            fib_list = b
    if method =="max" :
        while n > (fib_list[-1]+fib_list[-2]):
            fib_list.append(fib_list[-1]+fib_list[-2])
        if n == 1:
            fib_list = [0]

    return fib_list


print fibonacci(50, method="nterm")
