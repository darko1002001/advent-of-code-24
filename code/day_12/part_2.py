import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
DIRECTIONS_2 = [(1, 0), (0, 1)]

type SetOfNodes = set[tuple[tuple[int, int], tuple[int, int]]]


def calculate_perimeter(grid: list[str], nodes: set[tuple[int, int]]) -> int:
    perimeter_nodes: SetOfNodes = set()
    for node in nodes:
        for d in DIRECTIONS:
            di, dj = d
            ni, nj = node[0] + di, node[1] + dj
            if (
                ni not in range(len(grid))
                or nj not in range(len(grid[0]))
                or (ni, nj) not in nodes
            ):
                perimeter_nodes.add((node, (ni, nj)))
    corners: SetOfNodes = set()
    for n1, n2 in perimeter_nodes:
        keep = True
        for d in DIRECTIONS_2:
            di, dj = d
            n1x = (n1[0] + di, n1[1] + dj)
            n2x = (n2[0] + di, n2[1] + dj)

            if (n1x, n2x) in perimeter_nodes:
                keep = False
        if keep:
            corners.add((n1, n2))
    return len(corners)


def solve(inputs: list[str]) -> int:
    regions = discover_regions(inputs)
    components: dict[int, set[tuple[int, int]]] = defaultdict(set)
    for coordinates, id_ in regions.items():
        components[id_].add(coordinates)
    sum = 0
    for items in components.values():
        area = len(items)

        sum += area * calculate_perimeter(inputs, items)
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
