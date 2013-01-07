"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
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

def smallest_positive_number(num):
    def biggest(i, num):
        a, b = 1, i
        while b <= num:
            a, b = b, a * i
        return a
            
    def multi_factor(primers):
        for i in primers:
            if i * i <= num:
                yield biggest(i, num)
            else:
                yield i
    primers = itertools.takewhile(lambda x: x < num, prime())
    return reduce(int.__mul__, multi_factor(primers))

print smallest_positive_number(20)
