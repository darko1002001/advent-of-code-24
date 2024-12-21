import logging
from functools import cache
from itertools import pairwise
from typing import Literal

from solutions.utils import (
    DIRECTIONS_ARROWS_MAP,
    Coordinate,
    read_numbers,
    traverse_grid,
)

logger = logging.getLogger(__name__)

DOOR_KEYPAD = ["789", "456", "123", " 0A"]
ARROW_KEYPAD = [" ^A", "<v>"]

type KeypadType = Literal["D", "A"]
type Keypad = list[str]
type Moves = str

KEYPADS: dict[KeypadType, Keypad] = {"D": DOOR_KEYPAD, "A": ARROW_KEYPAD}


def solve(inputs: list[str]) -> int:
    return sum([solve_code(input) for input in inputs])


def find_coordinate(keypad_type: KeypadType, value: str) -> Coordinate:
    keypad = KEYPADS[keypad_type]
    for i, j, key in traverse_grid(keypad):
        if key == value:
            return i, j
    raise ValueError(f"Not found {value} in {keypad}")


@cache
def route_keys(keypad: KeypadType, start: str, end: str) -> list[Moves]:
    s = find_coordinate(keypad, start)
    e = find_coordinate(keypad, end)
    best_paths = route(keypad, s, e)
    return best_paths


def route(keypad_type: KeypadType, start: Coordinate, end: Coordinate) -> list[Moves]:
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

    # filter out just the shortest paths from all possible paths
    shortest = 1000
    for m in all_moves:
        shortest = min(shortest, len(m))

    # all combinations end with a 'A' press
    best_paths = [moves + "A" for moves in all_moves if len(moves) == shortest]

    # filter just the best paths. those are the ones that don't have keypresses that repeat with other keypresses in-between. ^<^ will be removed because there is already ^^< which is better
    filtered_best_paths: list[str] = []
    for path in best_paths:
        seen_characters: set[str] = set()
        seen_characters.add(path[0])
        ok = True
        for i in range(1, len(path)):
            c = path[i]
            if c in seen_characters and c != path[i - 1]:
                ok = False
        if ok:
            filtered_best_paths.append(path)

    return filtered_best_paths


@cache
def get_path_length(keypad_type: str, start: str, end: str, depth: int = 0) -> int:
    paths = route_keys(keypad_type, start, end)
    if depth == 0:
        return len(paths[0])

    best_length = 1 << 50
    for path in paths:
        path = "A" + path
        path_length = 0
        for a, b in pairwise(path):
            path_length += get_path_length("A", a, b, depth - 1)

        best_length = min(best_length, path_length)

    return best_length


def solve_code(code: str) -> int:
    number_: int = read_numbers(code)[0]
    total_path_length = 0
    for a, b in pairwise("A" + code):
        total_path_length += get_path_length("D", a, b, 25)

    return total_path_length * number_
