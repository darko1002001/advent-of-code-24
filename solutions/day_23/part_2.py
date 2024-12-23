import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

type ConnectionId = str


def solve(inputs: list[str]) -> str:
    graph: dict[ConnectionId, set[ConnectionId]] = defaultdict(set)
    all_connections = [tuple(input.split("-")) for input in inputs]

    seen: set[ConnectionId] = set()
    for c in all_connections:
        l, r = c
        graph[l].add(r)
        graph[r].add(l)
        connection = sorted([l, r])
        seen.add(",".join(connection))

    while len(seen) > 0:
        next_seen: set[ConnectionId] = set()
        for s in seen:
            connections = s.split(",")
            next_connections: set[ConnectionId] = {
                connected_nodes for c in connections for connected_nodes in graph[c]
            }
            next_connections.difference_update(connections)

            for node in next_connections:
                if all(node in graph[c] for c in connections):
                    new_connections = sorted(connections + [node])
                    next_seen.add(",".join(new_connections))
        seen = next_seen
        # it is going to be the largest group, there is a single largest group
        if len(next_seen) == 1:
            password = next(iter(next_seen))
            return password

    return ""
