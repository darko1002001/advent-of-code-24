from solutions.types import Section


def solve(inputs: Section) -> int:
    a: list[int] = []
    b: list[int] = []
    diff = 0
    for input in inputs:
        ax, bx = map(int, input.split("   "))
        a.append(ax)
        b.append(bx)
    a.sort()
    b.sort()
    for left, right in zip(a, b):
        diff += abs(right - left)
    return diff
