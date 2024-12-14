import logging
from typing import Literal, override

logger = logging.getLogger(__name__)


class Block:
    id: int
    category: Literal["space", "file"]
    size: int

    def __init__(self, id: int, category: Literal["space", "file"], size: int) -> None:
        self.id = id
        self.category = category
        self.size = size

    @override
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


def calculate_checksum(result_list: list[Block]):
    id = 0
    sum = 0
    for block in result_list:
        for _ in range(block.size):
            sum += block.id * id
            id += 1
    return sum


def solve(inputs: list[str]) -> int:
    disk_map = inputs[0]
    partition_list = read_blocks(disk_map)

    start = 0
    end = len(partition_list) - 1
    result_list: list[Block] = []

    while start < end:
        start_block = partition_list[start]
        end_block = partition_list[end]

        if start_block.category == "file":
            result_list.append(start_block)
            start += 1
            continue
        if start_block.size == 0:
            start += 1
            continue

        if end_block.category == "space" or end_block.size == 0:
            end -= 1
            continue
        if start_block.size < end_block.size:
            new_size = start_block.size
            end_block.size -= new_size
            start += 1
        elif start_block.size == end_block.size:
            new_size = start_block.size
            start += 1
            end -= 1
        else:
            new_size = end_block.size
            start_block.size -= new_size
            end -= 1

        new_block = Block(end_block.id, "file", new_size)
        result_list.append(new_block)
    if partition_list[end].size > 0:
        result_list.append(partition_list[end])
    return calculate_checksum(result_list)
