from collections import defaultdict

from solutions.types import Section


def solve(inputs: Section) -> int:
    a: list[int] = []
    b: dict[int, int] = defaultdict(int)
    result = 0
    for input in inputs:
        ax, bx = map(int, input.split("   "))
        a.append(ax)
        b[bx] += 1
    for ax in a:
        result += b[ax] * ax
    return result
