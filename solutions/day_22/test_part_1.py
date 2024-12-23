from solutions.types import LoadTextCallable

from .part_1 import solve


def test_part_1_sample(load_text: LoadTextCallable):
    lines = load_text("input_test")
    assert solve(lines) == 37327623


def test_part_1(load_text: LoadTextCallable):
    lines = load_text("input")
    assert solve(lines) == 13753970725
