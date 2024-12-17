import logging
from typing import override

from solutions.utils import read_numbers

logger = logging.getLogger(__name__)


class Registry:
    a: int
    b: int
    c: int
    outputs: list[int]

    instruction: int = 0

    def __init__(self, inputs: list[str]) -> None:
        self.a = read_numbers(inputs[0])[0]
        self.b = read_numbers(inputs[1])[0]
        self.c = read_numbers(inputs[2])[0]
        self.outputs = []

    def __getitem__(self, order: int) -> int:
        if order == 0:
            return self.a
        if order == 1:
            return self.b
        if order == 2:
            return self.c
        raise ValueError(f"Missing registry entry for {order}")

    def next_instruction(self):
        self.instruction += 2

    @override
    def __repr__(self):
        return f"{self.a}, {self.b}, {self.c}"


def combo_value(reg: Registry, value: int) -> int:
    if value <= 3:
        return value

    return reg[value - 4]


def adv(reg: Registry, value: int):
    """
    The adv instruction (opcode 0) performs division. The numerator is the value in the A register.
    The denominator is found by raising 2 to the power of the instruction's combo operand.
    (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
    The result of the division operation is truncated to an integer and then written to the A register.
    """
    combo = combo_value(reg, value)
    result: int = reg.a // pow(2, combo)
    reg.a = result
    reg.next_instruction()


def bxl(reg: Registry, value: int):
    """The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B."""
    reg.b = reg.b ^ value
    reg.next_instruction()


def bst(reg: Registry, value: int):
    """The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register."""
    combo = combo_value(reg, value)
    reg.b = combo % 8
    reg.next_instruction()


def jnz(reg: Registry, value: int):
    """The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero,
    it jumps by setting the instruction pointer to the value of its literal operand;
    if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    """
    if reg.a == 0:
        reg.next_instruction()
    elif reg.instruction == value:
        reg.next_instruction()
    else:
        reg.instruction = value


def bxc(reg: Registry, value: int):
    """The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons,
    this instruction reads an operand but ignores it.)"""
    reg.b = reg.b ^ reg.c
    reg.next_instruction()


def out(reg: Registry, value: int):
    """The out instruction (opcode 5) calculates the value of its combo operand modulo 8,
    then outputs that value. (If a program outputs multiple values, they are separated by commas.)
    """
    combo = combo_value(reg, value)
    reg.outputs.append(combo % 8)
    reg.next_instruction()


def bdv(reg: Registry, value: int):
    """The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register.
    (The numerator is still read from the A register.)"""
    combo = combo_value(reg, value)
    result: int = reg.a // pow(2, combo)
    reg.b = result
    reg.next_instruction()


def cdv(reg: Registry, value: int):
    """The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)"""
    combo = combo_value(reg, value)
    result: int = reg.a // pow(2, combo)
    reg.c = result
    reg.next_instruction()


def solve(inputs: list[str]) -> str:
    reg = Registry(inputs)

    program = read_numbers(inputs[4])
    logger.info(f"{reg=} {program=}")
    program_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}
    while reg.instruction < len(program):
        o, v = program[reg.instruction], program[reg.instruction + 1]
        program_map[o](reg, v)

    return ",".join(map(str, reg.outputs))
