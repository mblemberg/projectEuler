'''
Factorial digit sum

Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def fact(num) :
    sum = 1
    for i in range(1, int(num) + 1) :
        sum *= i
    return sum

def sumDigits(num) :
    sum = 0
    for digit in str(num) :
        sum += int(digit)
    return sum

x = fact(100)
print(f'100! = {x} and the sum of those digits is {sumDigits(x)}')

# 100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000 and the sum of those digits is 648