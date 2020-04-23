'''
Summation of primes
   
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

'''
Need a faster primality test for this one.  Also, when incrementing to find the next
prime, increment by 2, not one, since primes above 2 can only be odd.
'''

import array
import math

def isPrime(num):
    ''' use a layered approach.
        1. is it a multiple of a known prime? -> composite
        2. does it fail Fermat's test? -> composite
        3. finally, run the trial division test to determine primality
    '''

    if isPrimeFermat(num) and isPrimeTrial(num):
        return True
    else:
        return False

def isPrimeFermat(num):

    if num == 2 or num == 3:
        return True

    for a in range(2, min(10, num)):
        
        if num % a == 0:
            return False
        
        result = a ** (num - 1) % num
        
        if result != 1 and result != -1:
            return False
    else:
        return True

def isPrimeTrial(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num%i == 0:
            return False
    else:
        return True

def primesBelow(num):
    #use a sieve of Eratosthenes to genearte an array of all primes below num

    list = range(0, num)
    isPrime = [1]*len(list)
    isPrime[0] = isPrime[1] = 0

    for i in range(2, math.ceil(math.sqrt(num))):
        if isPrime[i]:
            for j in range(i + 1, num):
                if j % i == 0:
                    isPrime[j] = 0
    
    listOfPrimes = []

    for i in range(len(isPrime)):
        if isPrime[i]:
            listOfPrimes.append(list[i])

    return listOfPrimes

n = 7
sum = 17


while n < int(2E6):

    n += 2

    if isPrime(n):
        sum += n

else:
    print(f'The sum of all primes below two million is {sum}')