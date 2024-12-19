from .part_2 import solve


def test_part_2_sample(load_sections):
    lines = load_sections("input_test")
    assert solve(lines) == 16


def test_part_2(load_sections):
    lines = load_sections("input")
    assert solve(lines) == 650354687260341
