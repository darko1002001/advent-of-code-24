import heapq
import logging

from solutions.types import Coordinate, Grid
from solutions.utils import DIRECTIONS, traverse_grid

logger = logging.getLogger(__name__)

type Node = tuple[int, int, int]


def find_point(grid: Grid, to_find: str) -> Coordinate:
    for i, j, value in traverse_grid(grid):
        if value == to_find:
            return i, j
    raise ValueError(f"no {to_find} found")


def solve(grid: Grid, min_savings: int) -> int:
    grid = [list(input) for input in grid]
    start = find_point(grid, "S")
    end = find_point(grid, "E")
    walls: list[Coordinate] = []
    for i, j, value in traverse_grid(grid):
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
            continue
        if value == "#":
            walls.append((i, j))

    normal_steps, seen = find_exit(grid, start, end)

    cheats = 0
    for ai, aj in walls:
        explore = False
        for di, dj in DIRECTIONS:
            if (ai + di, aj + dj) in seen:
                explore = True
                break
        if not explore:
            continue
        grid[ai][aj] = "."
        cheat_steps, _ = find_exit(grid, start, end)
        grid[ai][aj] = "#"
        if cheat_steps <= normal_steps - min_savings:
            cheats += 1

    return cheats


def distance(i: int, j: int, ni: int, nj: int):
    return abs(i - ni) + abs(j - nj)


def find_exit(grid: Grid, start: Coordinate, end: Coordinate):
    pq: list[Node] = []
    heapq.heapify(pq)
    si, sj = start
    ei, ej = end
    seen: set[Coordinate] = set()
    heapq.heappush(pq, (0, si, sj))
    while len(pq) > 0:
        steps, i, j = heapq.heappop(pq)
        if i == ei and j == ej:
            return steps, seen
        if (i, j) in seen:
            continue
        seen.add((i, j))

        for d in DIRECTIONS:
            ni, nj = i + d[0], j + d[1]
            if (
                ni in range(1, len(grid) - 1)
                and nj in range(1, len(grid[0]) - 1)
                and grid[ni][nj] != "#"
            ):
                heapq.heappush(pq, (steps + 1, ni, nj))

    return 0, seen
