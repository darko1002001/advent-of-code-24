from .part_2 import solve


def test_part_2_small(load_sections):
    lines = load_sections("input_test_small_2")
    assert solve(lines) == 618


def test_part_2_sample(load_sections):
    lines = load_sections("input_test")
    assert solve(lines) == 9021


def test_part_2(load_sections):
    lines = load_sections("input")
    assert solve(lines) == 1522215
