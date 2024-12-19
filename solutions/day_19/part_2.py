import logging
from functools import cache

logger = logging.getLogger(__name__)


def solve(inputs: list[list[str]]) -> int:
    available, designs = inputs
    available = available[0].split(", ")

    return sum([can_make_design(available, design) for design in designs])


def can_make_design(available: list[str], design: str) -> int:

    @cache
    def can_make(current_index: int) -> int:
        if current_index >= len(design):
            return 1
        sum: int = 0
        for a in available:
            a_size = len(a)
            if design[current_index : current_index + a_size] == a:
                if count := can_make(current_index + a_size):
                    sum += count
        return sum

    return can_make(0)
