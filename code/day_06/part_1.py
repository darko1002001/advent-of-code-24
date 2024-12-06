import logging

logger = logging.getLogger(__name__)


def find_start(inputs: list[str]) -> tuple[int, int]:
    for i, row in enumerate(inputs):
        for j, col in enumerate(row):
            if col == "^":
                return i, j
    raise ValueError("No start found")


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve(inputs: list[str]) -> int:
    start = find_start(inputs)
    current_direction_index = 0
    current_position = start
    seen: set[tuple[int, int]] = set({start})
    while True:
        i, j = current_position
        di, dj = DIRECTIONS[current_direction_index]
        ni = i + di
        nj = j + dj
        if ni < 0 or nj < 0 or ni >= len(inputs) or nj >= len(inputs[0]):
            break
        if inputs[i + di][j + dj] != "#":
            current_position = (i + di, j + dj)
            seen.add(current_position)
        else:
            current_direction_index = (current_direction_index + 1) % len(DIRECTIONS)

    return len(seen)
