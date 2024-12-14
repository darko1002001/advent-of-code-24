import logging
import re

logger = logging.getLogger(__name__)


def solve(inputs: list[str]) -> int:
    return sum([solve_one(input) for input in inputs])


def solve_one(input: str) -> int:
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    groups = pattern.finditer(input)
    return sum([int(m.group(1)) * int(m.group(2)) for m in groups])
