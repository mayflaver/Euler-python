

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_square_difference(num):
    number1 = reduce(int.__add__, map(lambda x: x * x, range(1, num)))
    number2 = reduce(int.__add__, range(1, num+1))
    return number2 * number2 - number1

print sum_square_difference(10)
