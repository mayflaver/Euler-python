"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
def sum_multi3_and_multi5(num):
    return reduce(int.__add__, filter(lambda x: x%3 ==0 or x%5 == 0, range(1, num)))

print sum_multi3_and_multi5(1000)
