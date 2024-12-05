from .part_2 import solve


def test_part_2_sample(load_sections):
    lines = load_sections("part2_test")
    assert solve(lines) == 123


def test_part_2(load_sections):
    lines = load_sections("part2")
    assert solve(lines) == 5353
