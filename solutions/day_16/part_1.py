import heapq
import logging

from solutions.types import Grid
from solutions.utils import DIRECTIONS_MAP, traverse_grid

logger = logging.getLogger(__name__)

type Coordinate = tuple[int, int]
type Node = tuple[int, str, int, int]

DIRECTION_COSTS = {
    "R": [("R", 0), ("U", 1000), ("D", 1000), ("L", 2000)],
    "L": [("L", 0), ("U", 1000), ("D", 1000), ("R", 2000)],
    "U": [("U", 0), ("R", 1000), ("L", 1000), ("D", 2000)],
    "D": [("D", 0), ("R", 1000), ("L", 1000), ("U", 2000)],
}


def find_location(grid: Grid, search: str) -> Coordinate:
    for i, j, value in traverse_grid(grid):
        if value == search:
            return (i, j)
    raise ValueError(f"{search} Not found")


def solve(grid: Grid) -> int:
    si, sj = find_location(grid, "S")
    ei, ej = find_location(grid, "E")
    pq: list[Node] = []
    heapq.heapify(pq)
    heapq.heappush(pq, (0, "R", si, sj))
    visited: set[Coordinate] = set()
    while pq:
        item = heapq.heappop(pq)
        cost, direction, i, j = item
        visited.add((i, j))
        if i == ei and j == ej:
            return cost
        for next_direction, turn_cost in DIRECTION_COSTS[direction]:
            di, dj = DIRECTIONS_MAP[next_direction]
            ni, nj = i + di, j + dj
            if (ni, nj) in visited:
                continue
            if grid[ni][nj] != "#":
                heapq.heappush(pq, (cost + 1 + turn_cost, next_direction, ni, nj))

    return 0
