#!/usr/bin/python3
""" This module contains a program that solves the N queens problem """

import sys


def print_usage_and_exit(message, status):
    """ Usage error handling """
    print(message)
    sys.exit(status)


def is_valid(board, row, col):
    """ Validating position on board """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N):
    """ Program to solve N queens problem """
    def place_queens(row):
        """ Positions queens on board """
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
        else:
            for col in range(N):
                if is_valid(board, row, col):
                    board[row] = col
                    place_queens(row + 1)

    board = [-1] * N
    solutions = []
    place_queens(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N", 1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number", 1)

    if N < 4:
        print_usage_and_exit("N must be at least 4", 1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
