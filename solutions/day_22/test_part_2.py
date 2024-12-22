from .part_2 import solve


def test_part_2_sample(load_text):
    lines = load_text("input_test_2")
    assert solve(lines) == 23


def test_part_2(load_text):
    lines = load_text("input")
    assert solve(lines) == 1570
