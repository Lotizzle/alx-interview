#!/usr/bin/python3
"""
This module contains the isWinner(x, nums) method for finding the player
with the most wins in the prime game.
"""


def sieve(max_n):
    """ Returns an array where index indicates if it's a prime number. """
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, max_n + 1, i):
                is_prime[multiple] = False
    return is_prime


def count_primes(n, is_prime):
    """ Counts the number of primes up to n """
    return sum(is_prime[2:n+1])


def isWinner(x, nums):
    """ Determines the player with the most wins """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    is_prime = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = count_primes(n, is_prime)
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
