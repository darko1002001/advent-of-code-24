import logging
from collections import defaultdict

logger = logging.getLogger(__name__)


def solve(inputs: list[str]) -> int:
    rules = defaultdict(list)

    rules_section = inputs[0]

    rules_list = [rule.split("|") for rule in rules_section]
    for left, right in rules_list:
        rules[left].append(right)

    updates_section = inputs[1]
    seen = set()
    return sum([check_update(rules, update.split(",")) for update in updates_section])


def check_update(rules, update) -> int:
    seen = set()
    for value in update:
        value_rules = rules[value]
        for value_rule in value_rules:
            if value_rule in seen:
                return 0
        seen.add(value)
    middle = int(update[int(len(update) / 2)])
    return middle
