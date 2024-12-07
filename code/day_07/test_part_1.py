from .part_1 import solve


def test_part_1_sample(load_text):
    lines = load_text("part1_test")
    assert solve(lines) == 3749


def test_part_1(load_text):
    lines = load_text("part1")
    assert solve(lines) == 4555081946288
