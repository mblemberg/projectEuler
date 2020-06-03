'''
Amicable numbers

Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math

def d(n) :
    sum = 1
    for i in range(2, math.floor(math.sqrt(n))) :
        if n % i == 0 :
            sum += i + int(n/i)      # add i and its counter factor
    return sum

sum = 0
for a in range(2, 10000) :
    b = d(a)
    if a != b and d(b) == a :
        sum += a
print(f'The sum of all amicable pairs below 10000 is {sum}')
# The sum of all amicable pairs below 10000 is 31626