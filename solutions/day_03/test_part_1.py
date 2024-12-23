from solutions.types import LoadTextCallable

from .part_1 import solve


def test_part_1_sample(load_text: LoadTextCallable):
    lines = load_text("part1_test")
    assert solve(lines) == 161


def test_part_1(load_text: LoadTextCallable):
    lines = load_text("part1")
    assert solve(lines) == 173785482
