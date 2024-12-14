import logging

logger = logging.getLogger(__name__)


def solve(inputs: list[str]) -> int:
    blinks = 25
    stones = inputs[0].split(" ")
    for _ in range(blinks):
        stones = simulate(stones)
    return len(stones)


def simulate(stones: list[str]) -> list[str]:
    results: list[str] = []
    for stone in stones:
        if stone == "0":
            results.append("1")
        elif len(stone) % 2 == 0:
            results.append(str(int(stone[: len(stone) // 2])))
            results.append(str(int(stone[len(stone) // 2 :])))
        else:
            new_stone = str(int(stone) * 2024)
            results.append(new_stone)
    return results
