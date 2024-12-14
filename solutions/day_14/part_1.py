import logging
import math

from solutions.utils import read_numbers

logger = logging.getLogger(__name__)

SIMULATION_LENGTH = 100


def print_robots(end_positions: list[tuple[int, int]], size: tuple[int, int]):
    sx, sy = size
    grid = [sx * [0] for _ in range(sy)]
    for x, y in end_positions:
        grid[y][x] += 1
    for row in grid:
        logger.info("".join(map(str, row)))


def count_robots(end_positions: list[tuple[int, int]], size: tuple[int, int]) -> int:
    quadrants = [0, 0, 0, 0]
    size_x, size_y = size
    border_x = size_x // 2
    border_y = size_y // 2
    for x, y in end_positions:
        if x == border_x:
            continue
        if y == border_y:
            continue
        if x < border_x:
            if y < border_y:
                quadrants[0] += 1
            else:
                quadrants[1] += 1
        else:
            if y < border_y:
                quadrants[2] += 1
            else:
                quadrants[3] += 1
    logger.info(quadrants)
    return math.prod(quadrants)


def solve(inputs: list[str], size: tuple[int, int]) -> int:
    values = [read_numbers(row) for row in inputs]
    end_positions = [simulate_robot(value, size) for value in values]
    print_robots(end_positions, size)
    return count_robots(end_positions, size)


def simulate_robot(value: list[int], size: tuple[int, int]) -> tuple[int, int]:
    position_x, position_y, velocity_x, velocity_y = value
    size_x, size_y = size
    position_x += velocity_x * SIMULATION_LENGTH
    position_y += velocity_y * SIMULATION_LENGTH

    end_value = (position_x % size_x, position_y % size_y)
    return end_value
