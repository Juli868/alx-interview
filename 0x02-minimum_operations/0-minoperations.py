#!/usr/bin/python3
""" Determine the minimum operations required."""


def minOperations(n):
    """Return the minimum steps to take."""
    if n <= 1:
        return 0
    primes = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            primes.append(divisor)
            n //= divisor
        divisor += 1
    total = 0
    for num in primes:
        total += num
    return total
