'''
Project Euler problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def isDivisibleByAll(num, maxFactor):
    for i in range(1, maxFactor + 1):
        if num % i != 0:
            return False
    else:
        return True

i = 2520
while True:
    if isDivisibleByAll(i, 20):
        break
    i += 60
    # can speed this up if I increment by the least common multiple instead of by 20
    # can use this link to do it: http://www.math.com/school/subject1/lessons/S1U3L3DP.html

print(f'The smallest positive number that is evenly divisible by all numbers from 1 to 20 is {i}')

# The smallest positive number that is evenly divisible by all numbers from 1 to 20 is 232792560