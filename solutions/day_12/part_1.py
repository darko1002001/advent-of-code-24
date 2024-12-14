import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve(inputs: list[str]) -> int:
    regions = discover_regions(inputs)
    components: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for coordinates, id_ in regions.items():
        components[id_].append(coordinates)
    sum = 0
    for component, items in components.items():
        perimeter = 0
        for item_ in items:
            perimeter += calculate_perimeter(inputs, item_)
        sum += len(items) * perimeter
    return sum


def traverse_grid(grid: list[str]):
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            yield i, j, item


def discover_regions(grid: list[str]) -> dict[tuple[int, int], int]:
    seen: dict[tuple[int, int], int] = {}
    id_ = 0
    for i, j, _ in traverse_grid(grid):
        if (i, j) not in seen:
            discover_area(grid, seen, i, j, id_)
            id_ += 1
    return seen


def discover_area(
    grid: list[str], seen: dict[tuple[int, int], int], i: int, j: int, id_: int
):
    seen[i, j] = id_
    for d in DIRECTIONS:
        di = i + d[0]
        dj = j + d[1]
        if di not in range(len(grid)) or dj not in range(len(grid[0])):
            continue
        if (di, dj) in seen:
            continue
        if grid[di][dj] != grid[i][j]:
            continue
        discover_area(grid, seen, di, dj, id_)


def calculate_perimeter(grid: list[str], item_: tuple[int, int]) -> int:
    i, j = item_
    count = 0
    for d in DIRECTIONS:
        di = i + d[0]
        dj = j + d[1]
        if di < 0 or dj < 0 or di >= len(grid) or dj >= len(grid[0]):
            count += 1
        elif grid[di][dj] != grid[i][j]:
            count += 1
    return count
