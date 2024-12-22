import logging

logger = logging.getLogger(__name__)


def solve(inputs: list[str]) -> int:
    return sum([solve_input(input) for input in inputs])


def mix(a: int, b: int) -> int:
    return a ^ b


def prune(a: int) -> int:
    return a % 16777216


def next_secret(num: int) -> int:
    s1 = num * 64
    num = mix(num, s1)
    num = prune(num)
    s2 = num // 32
    num = mix(num, s2)
    num = prune(num)
    s3 = num * 2048
    num = mix(num, s3)
    num = prune(num)
    return num


def solve_input(input: str) -> int:
    num = int(input)
    for _ in range(2000):
        num = next_secret(num)
    return num
