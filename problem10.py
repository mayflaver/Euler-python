# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import itertools
import math
def prime():
    yield 2
    for i in itertools.count(3, 1):
        sentinel = math.sqrt(i)
        for p in prime():
            if p > sentinel:
                yield i
                break
            if i % p == 0:
                break

def Summation_of_primes(sum):
    return reduce(lambda x, y: x + y, itertools.takewhile(lambda x: x < sum, prime()))

print Summation_of_primes(2*10**6)
