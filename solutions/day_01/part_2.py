from collections import defaultdict


def solve(inputs) -> int:
    a = []
    b = defaultdict(int)
    result = 0
    for input in inputs:
        ax, bx = map(int, input.split("   "))
        a.append(ax)
        b[bx] += 1
    for ax in a:
        result += b[ax] * ax
    return result
