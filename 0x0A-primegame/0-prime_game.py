#!/usr/bin/python3
"""
Prime Game Module

This module contains the implementation of the isWinner function,
which determines the winner of the Prime Game played between Maria and Ben.
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
    x (int): The number of rounds.
    nums (list): An array of n values for each round.

    Returns:
    str: Name of the player that won the most rounds (Maria or Ben).
    None: If the winner cannot be determined.

    The game rules:
    - Players take turns choosing a prime number from a set of consecutive integers.
    - The chosen number and its multiples are removed from the set.
    - The player who cannot make a move loses the game.
    - Maria always goes first.
    """
    def is_prime(n):
        """
        Check if a number is prime.

        Args:
        n (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        """
        Get all prime numbers up to n.

        Args:
        n (int): The upper limit.

        Returns:
        list: A list of prime numbers up to n.
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_game(n):
        """
        Simulate a single game and determine the winner.

        Args:
        n (int): The upper limit of the set of integers for the game.

        Returns:
        str: The name of the winner (Maria or Ben).
        """
        primes = get_primes(n)
        if not primes:
            return "Ben"
        return "Maria" if len(primes) % 2 == 1 else "Ben"

    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
