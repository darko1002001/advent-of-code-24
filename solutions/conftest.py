import inspect
import pathlib

import pytest

from solutions.types import LoadSectionsCallable, LoadTextCallable, Section


@pytest.fixture
def load_text() -> LoadTextCallable:
    def load(name: str) -> Section:
        caller_file = inspect.stack()[1].filename
        path = pathlib.Path(caller_file).resolve().parent / f"{name}.txt"
        with open(path, "r") as file:
            return [line.rstrip("\n") for line in file.readlines()]

    return load


@pytest.fixture
def load_sections() -> LoadSectionsCallable:
    def load(name: str) -> list[Section]:
        caller_file = inspect.stack()[1].filename
        path = pathlib.Path(caller_file).resolve().parent / f"{name}.txt"
        with open(path, "r") as file:
            sections = file.read().strip().split("\n\n")
            return [section.split("\n") for section in sections]

    return load
