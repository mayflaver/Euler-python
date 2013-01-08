# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
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

def pos_prime(num):
    count = 1
    for i in prime():
        if count == num:
            return i
        else:
            count += 1

print pos_prime(10001)
