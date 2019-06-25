def gcd(a, b):
    #return the gcf of a and b using Euclid algorthim def gcd(a, b):
    while a !=0:
        a , b =b%a, a
    return b

def finModInverse(a, m):
    #return the modular  inverseof n %m, which is
    #the number x such that "x" % m= 1

    if(gcd) != 1:
        return None

    #Calculade using the Eucledian algorithm
    u1, u2, u3 = 1,0, a
    v1, v2, v3 = 0 , 1, m

    while v3 != 0:
        q = u3 //v3 
        v1,v2,v3, u1,u2,u3 = (u1 - q * v1),(u2 - q * v2), (u3 - q * v3),v1,v2, v3
        return u1 % m