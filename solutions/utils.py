import re


def read_numbers(value: str) -> list[int]:
    pattern = re.compile(r"(-?\d+)")
    iter_ = pattern.finditer(value)
    return list(map(int, [i.group(1) for i in iter_]))
