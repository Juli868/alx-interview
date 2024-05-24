#!/usr/bin/python3
"""Lock box unlocking."""


def canUnlockAll(boxes):
    """Determine if all locked boxes are un locked."""
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if key < n:
                    stack.append(key)

    return len(visited) == n
