#!/usr/bin/python3
"""
This module contains a module designed to find the minimum amount
of operations needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    This method finds the minimum operations needed
    to return H (n times).

    Parameter: n
    """

    if n <= 1:
        return 0

    minOps = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            minOps += divisor
            n //= divisor
        divisor += 1
    return minOps
