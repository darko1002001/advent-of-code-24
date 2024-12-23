import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

type ConnectionId = str


def solve(inputs: list[str]) -> int:
    graph: dict[str, set[str]] = defaultdict(set)
    connections = [tuple(input.split("-")) for input in inputs]

    for c in connections:
        l, r = c
        graph[l].add(r)
        graph[r].add(l)

    results: set[tuple[str, str, str]] = set()
    for c in connections:
        l, r = c
        l_connections = graph[l]
        r_connections = graph[r]
        for key in graph:
            if key == l or key == r:
                continue
            if (
                not key.startswith("t")
                and not l.startswith("t")
                and not r.startswith("t")
            ):
                continue
            if key in r_connections and key in l_connections:
                result: list[str] = [l, r, key]
                result.sort()
                a, b, c = result
                results.add((a, b, c))

    return len(results)
