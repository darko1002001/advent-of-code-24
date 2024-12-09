import logging
from cmath import e
from typing import Literal, Optional

logger = logging.getLogger(__name__)


class Block:
    id: int
    category: Literal["space", "file"]
    size: int

    def __init__(self, id: int, category: Literal["space", "file"], size: int) -> None:
        self.id = id
        self.category = category
        self.size = size

    def __repr__(self) -> str:
        word = "." if self.category == "space" else f"{self.id}"
        return word * self.size


def read_blocks(disk_map: str) -> list[Block]:
    partition_list: list[Block] = []
    id = 0
    for index, item in enumerate(disk_map):
        if index % 2 == 1:
            category = "space"
            id_ = 0
        else:
            category = "file"
            id_ = id
            id += 1
        partition_list.append(Block(id_, category, int(item)))
    return partition_list


def solve(inputs: list[str]) -> int:
    disk_map = inputs[0]
    partition_list = read_blocks(disk_map)

    end = len(partition_list) - 1
    while end >= 0:
        end_block = partition_list[end]

        if end_block.category == "space" or end_block.size == 0:
            end -= 1
            continue

        start = 0
        while start <= end:
            start_block = partition_list[start]
            if start_block.category == "file":
                start += 1
                continue

            if start_block.size == 0:
                start += 1
                continue

            if start_block.size == end_block.size:
                partition_list[start] = end_block
                partition_list[end] = start_block
                start += 1
                break
            if start_block.size > end_block.size:
                start_block.size -= end_block.size
                partition_list[end] = Block(0, "space", end_block.size)
                partition_list.insert(start, end_block)
                break
            start += 1

        end -= 1

    sum = 0
    id = 0
    for block in partition_list:
        if block.category == "space":
            id += block.size
            continue
        for _ in range(block.size):
            sum += block.id * id
            id += 1
    return sum
