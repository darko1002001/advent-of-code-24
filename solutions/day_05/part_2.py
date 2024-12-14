import logging
from collections import defaultdict
from functools import cmp_to_key

logger = logging.getLogger(__name__)


def solve(inputs: list[str]) -> int:
    rules: dict[int, list[int]] = defaultdict(list)

    rules_section = inputs[0]

    rules_list = [[int(r) for r in rule.split("|")] for rule in rules_section]
    for left, right in rules_list:
        rules[left].append(right)

    updates_section = inputs[1]
    return sum(
        [
            check_update(rules, [int(u) for u in update.split(",")])
            for update in updates_section
        ]
    )


def check_update(rules: dict[int, list[int]], update: list[int]) -> int:
    seen: set[int] = set()
    for value in update:
        value_rules = rules[value]
        for value_rule in value_rules:
            if value_rule in seen:
                return sort_update(rules, update)
        seen.add(value)
    return 0


def sort_update(rules: dict[int, list[int]], update: list[int]) -> int:
    def sort_by(a: int, b: int):
        value_rules = rules[a]
        if b in value_rules:
            return 1
        value_rules = rules[b]
        if a in value_rules:
            return -1
        return 0

    update.sort(key=cmp_to_key(sort_by))

    middle = update[len(update) // 2]
    return middle
