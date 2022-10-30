from collections import deque

from core.node import Node


def bfs(graph, function, stop_condition):
    results = []
    visited = set()
    waiting = deque([graph.root])
    running = True
    index = 0

    while len(waiting) > 0 and running:
        node: Node = waiting[0]
        waiting.popleft()
        
        if node in visited:
            continue

        visited.add(node)
        results.append(function(node, index))

        for children in list(node.pointers.values()):
            if children not in visited:
                waiting.append(children)

        running = not stop_condition(node, index)
        index += 1

    return results

def dfs(graph, function, stop_condition):
    results = []
    visited = set()
    waiting = deque([graph.root])
    running = True
    index = 0

    while len(waiting) > 0 and running:
        node: Node = waiting[-1]
        waiting.pop()
        
        if node in visited:
            continue

        visited.add(node)
        results.append(function(node, index))

        for children in list(node.pointers.values()):
            if children not in visited:
                waiting.append(children)

        running = not stop_condition(node, index)
        index += 1

    return results

FAMILIES = {
    "bfs": bfs,
    "dfs": dfs
}
