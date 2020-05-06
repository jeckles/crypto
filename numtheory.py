from decimal import *
getcontext().prec = 50  # set our precision to be very high


# Euler's totient function
def phi(n): 
    
    result = n   # initialze result as n 
    
    # consider all prime factors of n for every prime < square root of n
    p = 2 
    while(p * p <= n):  # for primes less than the square root of n 
        # check if p is a prime factor. 
        if (n % p == 0): 
            # if yes, update n and result 
            while (n % p == 0): 
                n = n // p # factor out p from n
            result = Decimal(result) * Decimal((Decimal(1.0) - (Decimal(1.0) / Decimal(p))))  # following book approach for calculating totient
        p = p + 1
          
          
    # if it is the case that n has a prime factor greater than its square root, then this can be the 
    # only one that is greater than n
    if (n > 1) : 
        result = result * Decimal(Decimal(1.0) - Decimal(Decimal(1.0) / Decimal(n))) 
   
    return int(result) 
