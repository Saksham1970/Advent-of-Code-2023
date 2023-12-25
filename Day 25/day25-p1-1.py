from collections import defaultdict
import random
from copy import deepcopy
from functools import reduce

graph = defaultdict(list)


with open("day25-input.txt", "r") as f:
    for i in f.readlines():
        node, neighbours = i.strip().split(":")
        neighbours = neighbours.strip().split()

        for neighbour in neighbours:
            graph[node].append(neighbour)
            graph[neighbour].append(node)

graph_old = graph

while True:
    graph = deepcopy(graph_old)
    edges_count = defaultdict(lambda: 1)

    #! Karger's Algorithm

    while len(graph) > 2:
        node = random.choice(tuple(graph.keys()))
        neighbour = random.choice(graph[node])

        for nn in graph[neighbour]:
            if nn != node:
                graph[node].append(nn)
                graph[nn].append(node)
            graph[nn] = [i for i in graph[nn] if i != neighbour]

        edges_count[node] += edges_count[neighbour]

        del graph[neighbour]
        del edges_count[neighbour]

    for node in graph:
        break

    if len(graph[node]) == 3:
        break

open("day25-output.txt", "w").write(
    str(reduce(lambda a, b: a * b, edges_count.values()))
)
