#!/usr/bin/python3
"""The 'Making Change' problem
"""


def makeChange(coins, total):
    """Find the number of coins needed to get to a certain amonunt(total)."""
    least_coins = 0
    if total <= 0:
        return least_coins
    coins.sort(reverse=True)
    for coin in coins:
        while total - coin >= 0:
            total -= coin
            least_coins += 1
        if total == 0:
            return least_coins

    return -1
