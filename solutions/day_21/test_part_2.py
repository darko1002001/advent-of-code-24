from .part_2 import solve


def test_part_2_sample(load_text):
    lines = load_text("input_test")
    assert solve(lines) == 154115708116294


def test_part_2(load_text):
    lines = load_text("input")
    assert solve(lines) == 246810588779586
