import heapq
import logging

from solutions.utils import DIRECTIONS, Coordinate, Grid, read_numbers

logger = logging.getLogger(__name__)


def solve(inputs: list[str], grid_size: int, simulate_count: int) -> int:
    coordinates = [tuple(reversed(read_numbers(input))) for input in inputs]
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    grid = [["."] * grid_size for _ in range(grid_size)]
    for idx in range(simulate_count):
        i, j = coordinates[idx]
        grid[i][j] = "#"
    return find_exit(grid, start, end, grid_size)


type Node = tuple[int, int, int]


def find_exit(grid: Grid, start: Coordinate, end: Coordinate, grid_size: int):
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
                ni in range(grid_size)
                and nj in range(grid_size)
                and grid[ni][nj] != "#"
            ):
                heapq.heappush(pq, (steps + 1, ni, nj))

    return 0
