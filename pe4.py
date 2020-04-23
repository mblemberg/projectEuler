'''
Project Euler problem #4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(num):
    
    num = str(num)

    if len(num) %2 != 0:
        return False

    for i in range(0, int(len(num)/2)):
        if num[i] != num[len(num)-i-1]:
            return False
    else:
        return True


def isProductOfThreeDigitnumbers(num):

    i = 999
    while i > 99:
        if num % i == 0 and num / i > 99 and num / i < 1000:
            return True
        i -= 1
    else:
        return False

'''
Will start with 999*999 and work downwards.
Check each number to see if it is a palindrome.
For each palindrome, factor it starting with the number itself and working down to 1.
When you find a number which is the product of two numbers > 99, stop.
'''

number = 999*999

# print(isProductOfThreeDigitnumbers(10000))
while number > 0:

    if isPalindrome(number) and isProductOfThreeDigitnumbers(number):
        print(f"The largest palindromic number which is a product of two three-digit numbers is: {number}")
        break
    
    number -= 1

# The largest palindromic number which is a product of two three-digit numbers is: 906609