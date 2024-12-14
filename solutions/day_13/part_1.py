import logging
import re

logger = logging.getLogger(__name__)

A_PRICE = 3
B_PRICE = 1


def solve_linear_system(
    aX: int, aY: int, aC: int, bX: int, bY: int, bC: int
) -> None | tuple[int, int]:
    determinant = aX * bY - aY * bX
    if determinant == 0:
        return None

    # Cramer's rule for solving 2x2 linear systems
    # Calculate numerators for a and b
    num_a = aC * bY - aY * bC
    num_b = aX * bC - aC * bX

    # Check divisibility
    if num_a % determinant == 0 and num_b % determinant == 0:
        a = num_a // determinant
        b = num_b // determinant
        return a, b
    return None


def solve(inputs: list[list[str]]) -> int:
    return sum([solve_item(input) for input in inputs])


def extract_button(value: str) -> tuple[int, int]:
    return extract(value, r"\+(\d+)")


def extract_prize(value: str) -> tuple[int, int]:
    return extract(value, r"=(\d+)")


def extract(value: str, regex: str) -> tuple[int, int]:
    pattern = re.compile(regex)
    groups = pattern.finditer(value)
    results = list([int(group.group(1)) for group in groups])
    return results[0], results[1]


def solve_item(input: list[str]) -> int:
    button_a, button_b, prize = input
    ax, ay = extract_button(button_a)
    bx, by = extract_button(button_b)
    prize_x, prize_y = extract_prize(prize)

    """

    # aX * pressA + bx * pressB = prizeX
    # aY * pressA + bY * pressB = prizeY
    # pressA = ?
    # pressB = ?

    """

    result = solve_linear_system(ax, bx, prize_x, ay, by, prize_y)
    if result is None:
        return 0
    a, b = result
    return A_PRICE * a + b * B_PRICE
