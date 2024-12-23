from itertools import pairwise


def solve(inputs: list[str]) -> int:
    levels = [list(map(int, level.split(" "))) for level in inputs]
    return sum([solve_level(level) for level in levels])


def solve_level(level: list[int]):
    decreasing = None
    for a, b in pairwise(level):
        diff = a - b
        if abs(diff) > 3 or diff == 0:
            return 0
        if decreasing == None:
            decreasing = diff > 0
        elif decreasing is not (diff > 0):
            return 0
    return 1
