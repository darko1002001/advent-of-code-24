import logging

logger = logging.getLogger(__name__)


def solve(inputs: list[list[str]]) -> int:
    available, designs = inputs
    available = available[0].split(", ")
    return sum([can_make_design(available, design, 0) for design in designs])


def can_make_design(available: list[str], design: str, current_index: int = 0) -> bool:

    if current_index >= len(design):
        return True
    for a in available:
        a_size = len(a)
        if design[current_index : current_index + a_size] == a:
            if can_make_design(available, design, current_index + a_size):
                return True
    return False
