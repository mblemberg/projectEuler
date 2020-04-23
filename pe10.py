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
        if isPrimeTrial(i):

            j = 2 * i
            while j < num:
                isPrime[j] = 0
                j += i

    listOfPrimes = []

    for i in range(len(isPrime)):
        if isPrime[i]:
            listOfPrimes.append(list[i])

    return listOfPrimes


primeSum = sum(primesBelow(int(2E6)))
print(f'The sum of all primes below two million is {primeSum}')

# The sum of all primes below two million is 142913828922