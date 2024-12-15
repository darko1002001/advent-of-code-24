import logging

from solutions.day_15.part_2 import print_grid

logger = logging.getLogger(__name__)

type Grid = list[list[str]]
type Coordinate = tuple[int, int]

MOVEMENTS = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}


def traverse(grid: Grid):
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            yield i, j, item


def find_start(grid: Grid) -> Coordinate:
    for i, j, item in traverse(grid):
        if item == "@":
            return (i, j)
    raise ValueError("Start not found")


def calculate_sum(grid: Grid) -> int:
    sum = 0
    for i, j, item in traverse(grid):
        if item != "O":
            continue
        sum += i * 100 + j
    return sum


def in_range(grid: Grid, coordinate: Coordinate) -> bool:
    i, j = coordinate
    return True if i in range(len(grid)) and j in range(len(grid[0])) else False


def can_move(grid: Grid, current: Coordinate, direction: Coordinate) -> bool:
    i, j = current
    while True:
        i += direction[0]
        j += direction[1]
        item = grid[i][j]
        if item == "#":
            return False
        if item == ".":
            return True


def move(grid: Grid, current: Coordinate, direction: Coordinate) -> Coordinate:
    if not can_move(grid, current, direction):
        return current
    to_move = [current]
    explore = [current]
    while explore:
        i, j = explore.pop(0)
        next_ = i + direction[0], j + direction[1]
        ni, nj = next_
        item = grid[ni][nj]
        if item == "O":
            to_move.append(next_)
            explore.append(next_)
    while to_move:
        m = to_move.pop()
        move_item(grid, m, direction)
    return current[0] + direction[0], current[1] + direction[1]


def move_item(grid: Grid, current: Coordinate, direction: Coordinate):
    ni, nj = current[0] + direction[0], current[1] + direction[1]
    i, j = current

    temp = grid[ni][nj]
    grid[ni][nj] = grid[i][j]
    grid[i][j] = temp


def solve(inputs: list[list[str]]) -> int:
    grid, movements = inputs
    grid = [list(row) for row in grid]
    movements = "".join(movements)
    current = find_start(grid)
    for movement in movements:
        current = move(grid, current, MOVEMENTS[movement])
    return calculate_sum(grid)
