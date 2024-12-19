from .part_1 import solve


def test_part_1_sample(load_sections):
    lines = load_sections("input_test")
    assert solve(lines) == 6


def test_part_1(load_sections):
    lines = load_sections("input")
    assert solve(lines) == 371
