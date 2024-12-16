from .part_1 import solve


def test_part_1_sample(load_text):
    lines = load_text("input_test")
    assert solve(lines) == 7036


def test_part_1_sample_2(load_text):
    lines = load_text("input_test_2")
    assert solve(lines) == 11048


def test_part_1(load_text):
    lines = load_text("input")
    assert solve(lines) == -1
