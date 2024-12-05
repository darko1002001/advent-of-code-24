import logging

logger = logging.getLogger(__name__)


def solve(inputs: list[str]) -> int:
    return sum(
        [
            check_x(inputs, r, c)
            for r, row in enumerate(inputs)
            for c, _ in enumerate(row)
            if inputs[r][c] == "A"
        ]
    )


def check_letter(inputs: list[str], r: int, c: int, letter: str) -> bool:
    if r >= len(inputs) or r < 0 or c >= len(inputs[0]) or c < 0:
        return False
    return inputs[r][c] == letter


def check_mas(inputs: list[str], r: int, c: int, direction: int) -> bool:
    if check_letter(inputs, r - 1, c - direction, "M") and check_letter(
        inputs, r + 1, c + direction, "S"
    ):
        return True
    if check_letter(inputs, r - 1, c - direction, "S") and check_letter(
        inputs, r + 1, c + direction, "M"
    ):
        return True
    return False


def check_x(inputs: list[str], r: int, c: int) -> bool:
    return check_mas(inputs, r, c, 1) and check_mas(inputs, r, c, -1)
