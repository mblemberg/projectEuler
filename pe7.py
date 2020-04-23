'''
Project Euler problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def isPrime(num):

    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num%i == 0:
            return False
    else:
        return True

def nextPrimeAbove(num):
    while True:
        num += 1
        if isPrime(num):
            return num
        
i=6 
lastPrime = 13
while i < 10001:
    lastPrime = nextPrimeAbove(lastPrime)
    i += 1

print(f'Prime number 10,001 is {lastPrime}')

# Prime number 10,001 is 104743
# This took a long time to run.  Should really speed up the primality check function