import logging

logger = logging.getLogger(__name__)

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def discover_trail(inputs: list[str], start: tuple[int, int]) -> int:
    seen: set[tuple[int, int]] = {start}
    q: list[tuple[int, int]] = [start]
    count = 0
    while q:
        item = q.pop()
        i, j = item
        if inputs[i][j] == "9":
            count += 1
        for di, dj in DIRECTIONS:
            ix = i + di
            jx = j + dj
            next_item = (ix, jx)
            if (
                in_range(inputs, next_item)
                and next_item not in seen
                and next_step(inputs, item, next_item)
            ):
                seen.add(next_item)
                q.append(next_item)
    return count


def in_range(inputs: list[str], item: tuple[int, int]) -> bool:
    i, j = item
    return i >= 0 and j >= 0 and i < len(inputs) and j < len(inputs[0])


def next_step(
    inputs: list[str], current: tuple[int, int], next: tuple[int, int]
) -> bool:
    return int(inputs[current[0]][current[1]]) + 1 == int(inputs[next[0]][next[1]])


def solve(inputs: list[str]) -> int:
    start = [
        (i, j)
        for i, row in enumerate(inputs)
        for j, item in enumerate(row)
        if item == "0"
    ]

    return sum([discover_trail(inputs, s) for s in start])
