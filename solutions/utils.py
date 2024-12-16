import re

type Grid = list[str] | list[list[str]]

DIRECTIONS_MAP = {"R": (0, 1), "U": (-1, 0), "D": (1, 0), "L": (0, -1)}
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

type Coordinate = tuple[int, int]


def traverse_grid(grid: Grid):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            yield i, j, value


def read_numbers(value: str) -> list[int]:
    pattern = re.compile(r"(-?\d+)")
    iter_ = pattern.finditer(value)
    return list(map(int, [i.group(1) for i in iter_]))
