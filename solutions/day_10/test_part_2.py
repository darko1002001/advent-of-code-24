from .part_2 import solve


def test_part_2_sample(load_text):
    lines = load_text("input_test")
    assert solve(lines) == 81


def test_part_2(load_text):
    lines = load_text("input")
    assert solve(lines) == 1034
