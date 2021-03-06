"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
import itertools

def fab(num):
    a, b = 0, 1
    while b <= num:
        yield b
        a, b = b, a+b

def sum_even_of_fab(num):
    return reduce(int.__add__, itertools.ifilter(lambda x: x%2 == 0, fab(num)))

print sum_even_of_fab(100)
