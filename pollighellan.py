# discrete log calculator, Pollig Hellman Algorithm

from decimal import *
getcontext().prec = 90  # set our precision to be very high

# utility function that should solve multiple congruences
def chinese_remainder_theorem(cngrs):
    if (len(cngrs) < 2):
        return None

    # in the case that there are only 2 functions to solve
    x0, mod0 = cngrs.pop(0)
    x1, mod1 = cngrs.pop(0)
    modinv0 = pow(mod0, -1, mod1)
    modinv1 = pow(mod1, -1, mod0)

    A = (modinv1 * mod1 * x0) + (modinv0 * mod0 * x1)
    newmod = mod0 * mod1
    resultx = A % newmod
    
    # now combine with the rest of the functions
    while(len(cngrs) != 0):
        x, mod = cngrs.pop(0)
        
        modinvx = pow(mod, -1, newmod)
        modinvy = pow(newmod, -1, mod)
        
        A = (modinvx * mod * resultx) + (modinvy * newmod * x)
        newmod = mod * newmod
        resultx = A % newmod

    return resultx
    print("oh whadduppp")
  

# this method generates a dictionary mapping prime number factors, stored as keys
# to their 
def gen_key_list(factors, a, p):
    primes = [i[0] for i in factors]
    result = {}
    result = dict.fromkeys(primes, None)
    for prime, exp in factors:
        if result[prime] is None:
            result[prime] = []
        i = 0
        while (i < prime):
            exponent = Decimal(i * Decimal((p - 1) // prime))
            result[prime].append(pow(a, exponent, p))
            i += 1
    return result

# this method computes the value of x mod whichever prime is passed in
def step(keys, pfac, exp, B, a, p):
    i = 0
    x = 0
    x_results = []
    result = 0
    while (i < exp):
        divby = pow(pfac, i + 1)
        findthis = pow(int(B), int((p - 1)//divby), int(p))
        for j in range(len(keys[pfac])):
            if (keys[pfac][j] == findthis):
                x = j  # this is going to be x
                x_results.append(x)
                break
        pexp = pow(pfac, i)
        multby = pow(a, -x * pexp, p)
        B = (B * multby) % p
        i += 1 
    for i in range(exp):
        result += pow(pfac, i) * x_results[i]
    return (result, pow(pfac, exp))  
        
def prime_factors(p):
    # since we expect to run this algorithm only when our p - 1 has small prime factor bases
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61] 
    results = []

    # basically all this does is continually divide p - 1 by its prime factors however many times they go into p - 1
    i = 0
    while ((p != 1) and (i < len(bases))):
        base = bases[i]
        exp = 0
        while((p % base) == 0):
            exp += 1
            p = p // base
        if (exp != 0):
            results.append((base, exp))
        i += 1
    return results

if __name__ == "__main__":
    p = 446140989947618904688678714274447794321069533419892517730557983492624382899857034042157
    B = 114001042708016081118647476597800778810296381669638296357404597997850983354180039247709
    a = 86
    
    # first thing generate a list of prime factors as well as their exponent
    factors = prime_factors(p - 1) 
   
    # next, create a dictionary where prime factors are the keys, denoted Qi
    # and values are a list of size i of their calculations of a^(k(p - 1)/Qi) for each k in range(1, i)
    keys = gen_key_list(factors, a, p)

    crt_this = []
    # now, loop through our factors to generate a dictionary of x mod our different prime factors
    for prime, exp in factors:
        crt_this.append(step(keys, prime, exp, B, a, p))

    # now all that is left to do is call CRT on our list
    discrete_log = chinese_remainder_theorem(crt_this)
    print("discrete log is ", discrete_log)
