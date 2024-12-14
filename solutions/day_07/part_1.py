import logging

logger = logging.getLogger(__name__)


def read_input_row(input: str) -> tuple[int, list[int]]:
    result, values = input.split(": ")
    values = map(int, values.split(" "))
    return int(result), list(values)


def solve(inputs: list[str]) -> int:
    return sum([solve_row(read_input_row(input)) for input in inputs])


def solve_row(input: tuple[int, list[int]]) -> int:
    result, values = input
    return result if operate(result, values, values[0], 1) else 0


def operate(result: int, values: list[int], current_result: int, index: int) -> bool:
    if index == len(values):
        return current_result == result

    return operate(
        result, values, current_result + values[index], index + 1
    ) or operate(result, values, current_result * values[index], index + 1)
