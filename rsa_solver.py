import math
from decimal import *
getcontext().prec = 50  # set our precision to be very high

e = 65537 # encryption exponent

# this method follows a p - 1 factorization based approach
def factor(n, i):
    # choose a value for a
    a = 2

    # this is our bound
    B = math.factorial(i)

    # compute a^B mod n 
    b0 = pow(a, B, n)

    # grab the gcd of (b0 - 1) and n
    gcd = math.gcd(b0 - 1, n)

    # if we get a non 1 or n value, we have found a factor of n
    if (gcd > 1 and gcd < n):
        return gcd
    else:
        return 0
        
if __name__ == "__main__":
    n = 58790927316372726348045786126195173874904045367 

    i = 0
    fac = 0
    while (fac == 0):
        fac = factor(n, i)
        i += 1
    print("one factor is ", fac)
    print("other factor is ", Decimal(Decimal(n)/Decimal(fac)))
    fac2 = Decimal(Decimal(n)/Decimal(fac))
    # now we have our factors, lets get d
   
    # first calculate phi
    phival = int((fac - 1) * (fac2 - 1))
    
    d = pow(e, -1, phival)
    
    # d = part_c.mod_inverse(e, phi_n)
    
    print("d is ", d)
    
    # now, decrypt message in part_a
    # first, make variable c
    c = 2108735695934471247327341278773563106066201068 
    
    print("decrypted message is ", pow(c, d, n))
