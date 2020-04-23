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

def isPrime(num):
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

def nextPrimeAbove(num):
    while True:
        num += 2
        if isPrimeFermat(num):
            return num

n = 7
sum = 17

while n < int(2E6):
    n = nextPrimeAbove(n)
    sum += n
else:
    print(f'The sum of all primes below two million is {sum}')