from .part_2 import solve


def test_part_2_sample(load_text):
    lines = load_text("input_test")
    assert solve(lines, 20) == 1449


def test_part_2(load_text):
    lines = load_text("input")
    assert solve(lines, 100) == 1005856
