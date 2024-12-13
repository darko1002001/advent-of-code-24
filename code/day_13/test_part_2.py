from .part_2 import solve


def test_part_2_sample(load_sections):
    lines = load_sections("input_test")
    assert solve(lines) == 875318608908


def test_part_2(load_sections):
    lines = load_sections("input")
    assert solve(lines) == 76358113886726
