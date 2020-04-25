'''
Longest Collatz sequence
   
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def outputChain(start):
    n = start
    print(start, end = ' ')

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n, end = ' ')

def chainLengthFrom(start):
    n = start
    length = 1
    while n != 1:
        if knownChainLengths[n]:
            return length + knownChainLengths[n]
        elif n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

knownChainLengths = [0 for i in range(0, int(1E6) + 1)]
global knownChainLengths
    # index represents starting point and the value is the chain length from that number
    # a value of 0 means that number has not been evaluated yet

longestChainLength = 0
for n in range(2, int(1E6)):
    

print(chainLengthFrom(13))