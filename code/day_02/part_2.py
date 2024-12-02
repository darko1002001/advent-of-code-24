import logging
from itertools import pairwise

logger = logging.getLogger(__name__)


def solve(inputs) -> int:
    inputs = [list(map(int, level.split(" "))) for level in inputs]
    return sum([solve_level_variations(level) for level in inputs])


def solve_level_variations(level: list[int]):
    is_ok = solve_level(level)
    if is_ok:
        return True
    for i in range(0, len(level)):
        if solve_level(sub_list(level, i)):
            return True
    return False


def sub_list(level, index):
    return level[:index] + level[(index + 1) :]


def solve_level(level: list[int]):
    decreasing = None
    for a, b in pairwise(level):
        diff = a - b
        if abs(diff) > 3 or diff == 0:
            return False
        if decreasing == None:
            decreasing = diff > 0
        elif decreasing is not (diff > 0):
            return False
    return True
