from .part_1 import solve


def test_part_1_sample(load_text):
    lines = load_text("input_test")
    assert solve(lines, (11, 7)) == 12


def test_part_1(load_text):
    lines = load_text("input")
    assert solve(lines, (101, 103)) == 229632480
