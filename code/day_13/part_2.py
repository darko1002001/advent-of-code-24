import logging
import re

import numpy

logger = logging.getLogger(__name__)

A_PRICE = 3
B_PRICE = 1


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
    prize_x += 10000000000000
    prize_y += 10000000000000

    """

    # aX * pressA + bx * pressB = prizeX
    # aY * pressA + bY * pressB = prizeY
    # pressA = ?
    # pressB = ?

    """

    left = [[ax, bx], [ay, by]]
    right = [prize_x, prize_y]
    result = numpy.linalg.solve(left, right)
    a, b = list([round(i) for i in result])
    correct_a: bool = (ax * a + bx * b) == prize_x
    correct_b: bool = (ay * a + by * b) == prize_y
    return A_PRICE * a + b * B_PRICE if correct_a and correct_b else 0
