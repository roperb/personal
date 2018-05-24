#Pythagorean Triple Generator

def pyTrip(n,m):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2+n**2
    return [a,b,c]
