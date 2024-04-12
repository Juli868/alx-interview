#!/usr/bin/python3
import sys

def placement(n: int) -> list[list[str]]:
    column = set()
    pos_diago = set()
    neg_diago = set()
    result = []
    board = [["."]for i in range(n)]
    def backtracking(r):
        if r == n:
            board_cpy ["".join(row) for row in board]
            result.append(board_cpy)
            return result
        for c in range()
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
placement(n)
