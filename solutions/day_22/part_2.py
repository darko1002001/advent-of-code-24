import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

type Price = tuple[int, PriceSequence]
type PriceSequence = tuple[int, int, int, int]
type BuyerDict = dict[PriceSequence, int]


def solve(inputs: list[str]) -> int:
    all_prices = [get_prices_for_buyer(input) for input in inputs]
    sequences: set[PriceSequence] = set()
    buyer_dicts: list[BuyerDict] = []
    for buyer_prices in all_prices:
        buyer_dict: BuyerDict = defaultdict(int)
        for price in buyer_prices:
            buy_price, sequence = price
            # monkeys will buy at first occurance of sequence
            if sequence not in buyer_dict:
                buyer_dict[sequence] = buy_price
            sequences.add(sequence)
        buyer_dicts.append(buyer_dict)

    global_max = 0
    for s in sequences:
        local_max = find_max(s, buyer_dicts)
        if local_max >= global_max:
            global_max = local_max
            logger.info(f"new max for sequence {s} {local_max=}")
    return global_max


def find_max(sequence: PriceSequence, buyers: list[BuyerDict]):
    sum = 0
    for _, b in enumerate(buyers):
        sum += b[sequence]
    return sum


def mix(a: int, b: int) -> int:
    return a ^ b


def prune(a: int) -> int:
    return a % 16777216


def next_secret(num: int) -> int:
    s1 = num * 64
    num = mix(num, s1)
    num = prune(num)
    s2 = num // 32
    num = mix(num, s2)
    num = prune(num)
    s3 = num * 2048
    num = mix(num, s3)
    num = prune(num)
    return num


def get_prices_for_buyer(
    input: str,
) -> list[Price]:
    num = int(input)
    diff = 0
    prices: list[Price] = []
    diff_sequence: list[int] = [0]
    for _ in range(2000):
        num_next = next_secret(num)
        buy_price = num_next % 10
        last_price = num % 10
        diff = buy_price - last_price
        diff_sequence.append(diff)
        if len(diff_sequence) > 4:
            _ = diff_sequence.pop(0)
        if len(diff_sequence) == 4:
            a, b, c, d = diff_sequence
            prices.append((buy_price, (a, b, c, d)))
        num = num_next
    return prices
