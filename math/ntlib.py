#Number Theory Library

def commonfactors(n,m):
    factors = []
    if n > m:
        n, m = m, n
    for i in range(1,m//2+1):
        if m%i == 0 and n%i == 0:
            factors.append(i)
    return factors
def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b

def findmodinverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


#Number Conversions
def digtobin(n):
    """
    Converts the a base 10 number to a binary number
    :param n:
    :return:
    """
    return int(bin(n)[2:])

def diglist(n):
    n = int(n)
    """
    Converts a number to a list of digits with the lowest digit being the first entry in the list
    :param n: input number
    :return: list of digits
    """
    digitlist = []
    while n > 0:
        digitlist.append(n%10)
        n //= 10
    return digitlist
def digtonum(list):
    """
    Takes a list of digits from lowest to highest and returns the number
    :param list: the list of digits from lowest to highest
    :return: the number made from those digits
    """
    num = 0
    for d in range(len(list)):
        num += list[d]*10**d
    return num

###Structure of Numbers

def ispalindrome(input):
    """
    :param input: input string or number
    :return: True if input is a palindrome
    """
    if type(input) != type(""):
        number = str(input)
    palCheckVal = 1
    for i in range(len(input) // 2):
        if input[i] != input[-(i + 1)]:
            palCheckVal = 0

    if palCheckVal == 1:
        return True
    else:
        return False

def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l
