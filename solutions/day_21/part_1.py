import logging
from functools import cache

from solutions.utils import (
    DIRECTIONS_ARROWS_MAP,
    Coordinate,
    read_numbers,
    traverse_grid,
)

logger = logging.getLogger(__name__)

DOOR_KEYPAD = ["789", "456", "123", " 0A"]
ARROW_KEYPAD = [" ^A", "<v>"]

type Keypad = list[str]
type Moves = str

KEYPADS = {"D": DOOR_KEYPAD, "A": ARROW_KEYPAD}


def solve(inputs: list[str]) -> int:
    return sum([solve_code(input) for input in inputs])


def find_coordinate(keypad_type: str, value: str) -> Coordinate:
    keypad = KEYPADS[keypad_type]
    for i, j, key in traverse_grid(keypad):
        if key == value:
            return i, j
    raise ValueError(f"Not found {value} in {keypad}")


@cache
def route_keys(keypad: str, start: str, end: str) -> list[Moves]:
    s = find_coordinate(keypad, start)
    e = find_coordinate(keypad, end)
    best_paths = route(keypad, s, e)
    return best_paths


def route(keypad_type: str, start: Coordinate, end: Coordinate) -> list[Moves]:
    keypad = KEYPADS[keypad_type]

    q: list[tuple[Coordinate, list[str], list[Coordinate]]] = []
    q.append((start, [], []))
    all_moves: list[Moves] = []
    while q:
        coordinate, path, seen = q.pop(0)
        seen = seen + [coordinate]

        if coordinate == end:
            all_moves.append("".join(path))
            continue
        i, j = coordinate
        for name, d in DIRECTIONS_ARROWS_MAP.items():
            di, dj = i + d[0], j + d[1]
            if di not in range(len(keypad)) or dj not in range(len(keypad[0])):
                continue
            if keypad[di][dj] == " ":
                continue
            if (di, dj) in seen:
                continue
            q.append(((di, dj), path + [name], seen))
    shortest = 1000
    for m in all_moves:
        shortest = min(shortest, len(m))
    best_paths = [moves + "A" for moves in all_moves if len(moves) == shortest]
    filtered_best_paths = []
    for p in best_paths:
        seen = set()
        seen.add(p[0])
        ok = True
        for i in range(1, len(p)):
            c = p[i]
            if c in seen and c != p[i - 1]:
                ok = False
        if ok:
            filtered_best_paths.append(p)

    return filtered_best_paths


def solve_robot(
    keypad_type: str, current_move: Moves, total_moves: int, results: set[str]
):
    if total_moves == 0:
        results.add(current_move)
        return

    start = "A"

    current_moves = set()
    current_moves.add("")
    for value in current_move:
        moves = route_keys(keypad_type, start, value)
        start = value

        next_moves = set()
        for c in current_moves:
            for m in moves:
                next_moves.add(c + m)
        current_moves = next_moves
    for move in current_moves:
        solve_robot("A", move, total_moves - 1, results)


def solve_code(code: str) -> int:
    logger.info(f"solving {code}")
    results: set[str] = set()
    solve_robot("D", code, 3, results)

    number_ = read_numbers(code)[0]

    shortest_code = min(results)
    logger.info(f"{shortest_code} {len(shortest_code)} * {number_}")
    return len(shortest_code) * number_
