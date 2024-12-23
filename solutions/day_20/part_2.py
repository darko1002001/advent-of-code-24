import heapq
import logging
from collections import defaultdict

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
    normal_steps = find_exit(grid, start, end)

    max_cost = normal_steps - min_savings

    cheats = 0
    distances_start = find_all_distances(grid, start)
    distances_end = find_all_distances(grid, end)
    for dsi, dsj in distances_start:
        for dei, dej in distances_end:
            dx = distance(dsi, dsj, dei, dej)
            if dx <= 20:
                if (
                    distances_start[(dsi, dsj)] + dx + distances_end[(dei, dej)]
                    <= max_cost
                ):
                    cheats += 1

    return cheats


def distance(i: int, j: int, ni: int, nj: int):
    return abs(i - ni) + abs(j - nj)


def find_all_distances(grid: Grid, start: Coordinate) -> dict[Coordinate, int | float]:
    q: list[Node] = []
    si, sj = start
    distances: dict[Coordinate, int | float] = defaultdict(lambda: float("inf"))
    q.append((0, si, sj))
    seen: set[Coordinate] = set()
    distances[start] = 0
    while q:
        steps, i, j = q.pop(0)
        if (i, j) in seen:
            continue
        seen.add((i, j))
        for d in DIRECTIONS:
            di, dj = d
            ni, nj = i + di, j + dj
            if (
                ni in range(len(grid))
                and nj in range(len(grid[0]))
                and grid[ni][nj] == "."
            ):
                if steps + 1 < distances[(ni, nj)]:
                    distances[(ni, nj)] = steps + 1
                    q.append((steps + 1, ni, nj))

    return distances


def find_exit(grid: Grid, start: Coordinate, end: Coordinate) -> int:
    pq: list[Node] = []
    heapq.heapify(pq)
    si, sj = start
    ei, ej = end
    seen: set[Coordinate] = set()
    heapq.heappush(pq, (0, si, sj))
    while len(pq) > 0:
        steps, i, j = heapq.heappop(pq)
        if i == ei and j == ej:
            return steps
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

    return 0
