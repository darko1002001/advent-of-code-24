from .part_1 import solve


def test_part_1_sample(load_sections):
    lines = load_sections("part1_test")
    assert solve(lines) == 143


def test_part_1(load_sections):
    lines = load_sections("part1")
    assert solve(lines) == 6384
