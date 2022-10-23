# Large Prime Generation for RSA
import random
from constants import sieve_primes
 
def nBitRandom(n):
    return random.randrange(10**(n-1)+1, 10**n - 1)
 
def getLowLevelPrime(n):
    while True:
        p = nBitRandom(n)
        for divisor in sieve_primes:
            if p % divisor == 0 and divisor**2 <= p:
                break
        else: 
            return p
 
def isProbablePrime(mrc):
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)
    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True
    numberOfTrials = 20 # Less than 10^-20 error in production
    for i in range(numberOfTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True

def genPrime(n):
    while True:
        prime_candidate = getLowLevelPrime(n)
        if not isProbablePrime(prime_candidate):
            continue
        return prime_candidate

def genPrimeBtwn(a, b):
    while True:
        p = random.randrange(a, b)
        prime_candidate = getLowLevelPrime(p)
        if not isProbablePrime(prime_candidate):
            continue
        return prime_candidate