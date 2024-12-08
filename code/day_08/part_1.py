import logging
from collections import defaultdict
from typing import TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


def run_pairs(values: list[T]):
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            yield values[i], values[j]


def in_range(inputs: list[str], coordinates: tuple[int, int]):
    i, j = coordinates
    return i >= 0 and j >= 0 and i < len(inputs) and j < len(inputs[0])


def calculate_range(a: tuple[int, int], b: tuple[int, int]):
    ax, ay = a
    bx, by = b
    dx = bx - ax
    dy = by - ay
    yield (ax - dx, ay - dy)
    yield (bx + dx, by + dy)


def solve(inputs: list[str]) -> int:
    groups: dict[str, list[tuple[int, int]]] = defaultdict(list)

    for i, row in enumerate(inputs):
        for j, val in enumerate(row):
            if val == ".":
                continue
            groups[val].append((i, j))
    results: set[tuple[int, int]] = set()

    for values in groups.values():
        for a, b in run_pairs(list(values)):
            for coordinates in calculate_range(a, b):
                if in_range(inputs, coordinates):
                    results.add((coordinates[0], coordinates[1]))
    return len(results)
