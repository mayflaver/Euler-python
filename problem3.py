"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
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

def largest_prime_factor(num):
    sentinel = math.sqrt(num)
    a = 0
    for p in prime():
        if p > sentinel:
            return a
        elif num % p == 0:
            a = p

print largest_prime_factor(600851475143) # maybe run long time, if you have a good idea, please tell me
