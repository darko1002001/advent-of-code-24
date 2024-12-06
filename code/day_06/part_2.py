import logging

logger = logging.getLogger(__name__)


def find_start(inputs: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(inputs):
        for j, col in enumerate(row):
            if col == "^":
                return i, j
    raise ValueError("No start found")


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def next_direction(current_direction_index: int):
    return (current_direction_index + 1) % len(DIRECTIONS)


def solve(inputs: list[str]) -> int:
    grid = [list(input) for input in inputs]
    start = find_start(grid)
    current_direction_index = 0
    barriers = 0
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item == "#":
                continue
            seen: set[tuple[int, int, int]] = set(
                {(start[0], start[1], current_direction_index)}
            )
            grid[i][j] = "#"
            barriers += solve_run(grid, seen, start, current_direction_index)
            grid[i][j] = "."

    return barriers


def solve_run(
    inputs: list[list[str]],
    seen: set[tuple[int, int, int]],
    start: tuple[int, int],
    current_direction_index: int,
) -> int:
    current_position = start
    while True:
        i, j = current_position

        di, dj = DIRECTIONS[current_direction_index]
        ni = i + di
        nj = j + dj
        if ni < 0 or nj < 0 or ni >= len(inputs) or nj >= len(inputs[0]):
            return 0

        if inputs[i + di][j + dj] != "#":
            current_position = (i + di, j + dj)
            next_check = (
                current_position[0],
                current_position[1],
                current_direction_index,
            )
            if next_check in seen:
                return 1
            seen.add(next_check)
        else:
            current_direction_index = next_direction(current_direction_index)
