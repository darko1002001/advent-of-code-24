import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

type ConnectionId = str


def solve(inputs: list[str]) -> str:
    graph: dict[str, set[str]] = defaultdict(set)
    all_connections = [tuple(input.split("-")) for input in inputs]

    nodes = graph.keys()
    password = ""
    seen: set[str] = set()
    for c in all_connections:
        l, r = c
        graph[l].add(r)
        graph[r].add(l)
        connection = [l, r]
        connection.sort()
        seen.add(",".join(connection))

    while len(seen) > 0:
        next_seen: set[str] = set()
        for s in seen:
            connections = s.split(",")
            for node in nodes:
                if node in connections:
                    continue
                connected = True
                for c in connections:
                    if node not in graph[c]:
                        connected = False
                        break
                if connected:
                    new_connections = connections + [node]
                    new_connections.sort()
                    next_seen.add(",".join(new_connections))
        seen = next_seen
        if len(next_seen) == 1:
            password = next(iter(next_seen))
            return password

    return ""
