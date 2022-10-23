from math import *

# Generate sieve list

n = 10**5 # Size of prime generation

def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(floor(sqrt(n))), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

Primes = [0] * n
def SieveOfEratosthenes(n) :
    Primes[0] = 1
    i = 3
    while(i * i <= n):
        if (Primes[i // 2] == 0):
            for j in range(3 * i, n+1, 2 * i):
                Primes[j // 2] = 1
        i += 2

f = open('primes_list.txt', 'w')
f.write('[2, ')
list_string = ""
SieveOfEratosthenes(n)
for i in range(3, n+1, 2):
    if (Primes[i // 2] == 0) :
        list_string += (str(i) + ', ')
f.write(list_string + ']')
f.close()