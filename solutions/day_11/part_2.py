import logging
from functools import cache

logger = logging.getLogger(__name__)


def solve(inputs: list[str]) -> int:
    blinks = 75
    stones = inputs[0].split(" ")
    return sum(split_stone(stone, blinks) for stone in stones)


@cache
def split_stone(stone: str, blinks: int) -> int:
    if blinks == 0:
        return 1
    sum = 0
    if stone == "0":
        sum += split_stone("1", blinks - 1)
    elif len(stone) % 2 == 0:
        sum += split_stone(str(int(stone[: len(stone) // 2])), blinks - 1)
        sum += split_stone(str(int(stone[len(stone) // 2 :])), blinks - 1)
    else:
        new_stone = str(int(stone) * 2024)
        sum += split_stone(new_stone, blinks - 1)

    return sum
