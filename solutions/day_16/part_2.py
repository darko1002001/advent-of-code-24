import heapq
import logging
from collections import defaultdict

from solutions.utils import DIRECTIONS_MAP, Grid, traverse_grid

logger = logging.getLogger(__name__)

type Coordinate = tuple[int, int]
type CoordinateWithDirection = tuple[int, int, str]
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

    min_cost: dict[CoordinateWithDirection, int | float] = defaultdict(
        lambda: float("inf")
    )

    all_paths: dict[CoordinateWithDirection, set[CoordinateWithDirection]] = (
        defaultdict(set)
    )

    end_direction = ""
    while pq:
        item = heapq.heappop(pq)
        cost, direction, i, j = item
        if i == ei and j == ej:
            if end_direction == "":
                end_direction = direction
            continue
        for next_direction, turn_cost in DIRECTION_COSTS[direction]:
            di, dj = DIRECTIONS_MAP[next_direction]
            next_ = i + di, j + dj
            ni, nj = next_
            next_directed = ni, nj, next_direction
            if grid[ni][nj] == "#":
                continue
            next_cost = cost + 1 + turn_cost
            if next_cost < min_cost[next_directed]:
                min_cost[next_directed] = next_cost
                all_paths[next_directed] = {(i, j, direction)}
                heapq.heappush(pq, (next_cost, next_direction, ni, nj))

            elif next_cost == min_cost[next_directed]:
                all_paths[next_directed].add((i, j, direction))

    stack = [(ei, ej, end_direction)]
    nodes = set(stack)
    while stack:
        item = stack.pop()
        for node in all_paths[item]:
            if node not in nodes:
                nodes.add(node)
                stack.append(node)
    solution_nodes = set([(x, y) for x, y, _ in nodes])
    return len(solution_nodes)
