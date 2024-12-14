def solve(inputs) -> int:
    a = []
    b = []
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
