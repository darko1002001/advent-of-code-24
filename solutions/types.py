from typing import Callable

type Grid = list[str] | list[list[str]]
type Coordinate = tuple[int, int]

type Section = list[str]
type LoadTextCallable = Callable[[str], Section]
type LoadSectionsCallable = Callable[[str], list[Section]]
