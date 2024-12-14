import logging
import math

from solutions.utils import read_numbers

logger = logging.getLogger(__name__)

SIMULATION_LENGTH = 10000


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
    return math.prod(quadrants)


def solve(inputs: list[str], size: tuple[int, int]) -> int:
    values = [read_numbers(row) for row in inputs]
    min_count = 1000000000000000
    last_sim_length = 0
    for i in range(1, SIMULATION_LENGTH):
        end_positions = [simulate_robot(value, size, i) for value in values]
        count_ = count_robots(end_positions, size)
        if min_count >= count_:
            min_count = count_
            # Found this visually. The count of total quadrats product would be the smallest when all the robots are grouped into a single place. 10k simulations should be enough to find it
            # optionally print the results and the simulation step to verify the image
            # print_robots(end_positions, size)
            # logger.info(f"simulation step {i}")
            last_sim_length = i
    return last_sim_length


def simulate_robot(
    value: list[int], size: tuple[int, int], simulation_length: int
) -> tuple[int, int]:
    position_x, position_y, velocity_x, velocity_y = value
    size_x, size_y = size
    position_x += velocity_x * simulation_length
    position_y += velocity_y * simulation_length

    end_value = (position_x % size_x, position_y % size_y)
    return end_value
