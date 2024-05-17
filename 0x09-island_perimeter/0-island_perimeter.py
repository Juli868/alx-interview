#!/usr/bin/python3
"""Calculating a perimeter of a grid."""
def island_perimeter(grid):
    """Return the perimeter."""
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                result += 4
                if grid[i][j-1] == 1:
                    result -= 2
                if grid[i-1][j] == 1:
                    result -= 2
    return result
