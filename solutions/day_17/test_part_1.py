from .part_1 import solve


def test_part_1_sample(load_text):
    lines = load_text("input_test")
    assert solve(lines) == "4,6,3,5,6,3,5,2,1,0"


def test_part_1(load_text):
    lines = load_text("input")
    assert solve(lines) == "1,7,6,5,1,0,5,0,7"
