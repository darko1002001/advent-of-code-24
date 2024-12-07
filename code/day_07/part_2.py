import logging

logger = logging.getLogger(__name__)


def read_input_row(input: str) -> tuple[int, list[str]]:
    result, values = input.split(": ")
    values = values.split(" ")
    return int(result), list(values)


def solve(inputs: list[str]) -> int:
    return sum([solve_row(read_input_row(input)) for input in inputs])


def solve_row(input: tuple[int, list[str]]) -> int:
    result, values = input
    return result if operate(result, values, int(values[0]), 1) else 0


def operate(result: int, values: list[str], current_result: int, index: int) -> bool:
    if index == len(values):
        return current_result == result

    return (
        operate(result, values, current_result + int(values[index]), index + 1)
        or operate(result, values, current_result * int(values[index]), index + 1)
        or operate(result, values, int(str(current_result) + values[index]), index + 1)
    )
