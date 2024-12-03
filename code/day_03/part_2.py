import logging
import re

logger = logging.getLogger(__name__)


def solve(inputs: list[str]) -> int:
    return solve_input("".join(inputs))


def solve_input(input: str) -> int:
    pattern = re.compile(r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)")
    groups = pattern.finditer(input)
    enabled = True
    sum = 0
    for m in groups:
        value = input[m.start() : m.end()]
        if value.startswith("don't"):
            enabled = False
        elif value.startswith("do"):
            enabled = True
        elif enabled:
            sum += int(m.group(1)) * int(m.group(2))
    return sum
