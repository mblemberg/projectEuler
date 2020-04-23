'''
Project Euler problem #3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

'''
Will follow the upside down long division method described here:

https://www.purplemath.com/modules/factnumb.htm


First, in order to make that work, need to create a primality test function

# https://en.wikipedia.org/wiki/Primality_test
'''

import math

given = 600851475143

#trial division primality test method (not fast)
def isPrime(num):

    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num%i == 0:
            return False
    else:
        return True

def firstPrimeFactor(num):
    #returns either the first (lowest) prime fator of num or -1 if it finds no prime factors

    if num < 2:
        return -1

    for i in range(2, num):

        if num % i ==0 and isPrime(i):
            return i
    else:
        return -1


def primeDivision(num):
    #https://www.purplemath.com/modules/factnumb.htm

    print(f'\nPerforming prime factorization for: {num}')

    while not isPrime(num):
        nextFactor = firstPrimeFactor(num)
        num = int(num / nextFactor)
        print(f'Next prime factor is: {nextFactor}')
    else:
        print(f'The last and largest prime factor is: {num}\n')

# primeDivision(1050)
primeDivision(given)

'''
Results:

Performing prime factorization for: 600851475143
Next prime factor is: 71
Next prime factor is: 839
Next prime factor is: 1471
The last and largest prime factor is: 6857
'''