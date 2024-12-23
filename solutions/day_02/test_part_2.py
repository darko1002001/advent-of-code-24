from solutions.types import LoadTextCallable

from .part_2 import solve


def test_part_2_sample(load_text: LoadTextCallable):
    lines = load_text("part2_test")
    assert solve(lines) == 4


def test_part_2(load_text: LoadTextCallable):
    lines = load_text("part2")
    assert solve(lines) == 301
