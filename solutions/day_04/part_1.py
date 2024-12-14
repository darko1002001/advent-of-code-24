import logging

logger = logging.getLogger(__name__)


def solve(inputs: list[str]) -> int:
    return sum(
        [check(inputs, r, c) for r, row in enumerate(inputs) for c, _ in enumerate(row)]
    )


WORD = "XMAS"


def check_direction(
    inputs: list[str], r: int, c: int, word_index: int, direction: tuple[int, int]
) -> int:
    if r >= len(inputs) or r < 0 or c >= len(inputs[0]) or c < 0:
        return 0
    if inputs[r][c] != WORD[word_index]:
        return 0
    if word_index == len(WORD) - 1:
        return 1

    di = direction[0]
    dj = direction[1]
    return check_direction(inputs, r + di, c + dj, word_index + 1, direction)


def check(inputs: list[str], r: int, c: int) -> int:
    sum = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            sum += check_direction(inputs, r, c, 0, (dr, dc))
    return sum
