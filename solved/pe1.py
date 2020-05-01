'''
Project Euler problem #1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import math

def sumMultiplesOf(n, upTo):
    sum = 0
    for i in range(1, math.ceil(upTo / n)):
        sum += i * n
    return sum

sum = sumMultiplesOf(3, 1000) + sumMultiplesOf(5, 1000) - sumMultiplesOf(15, 1000)
print(f'The sum of all multiples of 3 or 5 below 1000 is: {sum}')

# Sum of all multiples of 3 or 5 between 0 and 1000 is : 233168