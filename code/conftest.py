import inspect
import pathlib

import pytest


@pytest.fixture
def load_text():
    def load(name) -> list[str]:
        caller_file = inspect.stack()[1].filename
        path = pathlib.Path(caller_file).resolve().parent / f"{name}.txt"
        with open(path, "r") as file:
            return [line.rstrip("\n") for line in file.readlines()]

    return load


@pytest.fixture
def load_sections():
    def load(name) -> list[list[str]]:
        caller_file = inspect.stack()[1].filename
        path = pathlib.Path(caller_file).resolve().parent / f"{name}.txt"
        with open(path, "r") as file:
            sections = file.read().split("\n\n")
            return [section.split("\n") for section in sections]

    return load
