from .part_2 import solve


def test_part_2(load_text):
    lines = load_text("input")
    assert solve(lines, (101, 103)) == 7051
