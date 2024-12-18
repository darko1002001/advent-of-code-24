from .part_1 import solve


def test_part_1_sample(load_text):
    lines = load_text("input_test")
    assert solve(lines, 7, 12) == 22


def test_part_1(load_text):
    lines = load_text("input")
    assert solve(lines, 71, 1024) == 416
