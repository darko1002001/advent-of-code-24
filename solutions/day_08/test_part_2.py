from .part_2 import solve


def test_part_2_sample(load_text):
    lines = load_text("part2_test")
    assert solve(lines) == 34


def test_part_2(load_text):
    lines = load_text("part2")
    assert solve(lines) == 1190
