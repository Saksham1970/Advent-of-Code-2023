from collections import defaultdict
from itertools import count

with open("day23-input.txt", "r") as f:
    grid = [list(i.strip()) for i in f.readlines()]

for j in range(len(grid[0])):
    if grid[0][j] == ".":
        start = (0, j)

id_gen = count()

maze_graph = defaultdict(set)
stepsd = {}
end = [0]


def convert_maze_to_graph(r, c, graph_id):
    steps = 0

    while True:
        if r == len(grid) - 1:
            end[0] = graph_id

        nexts = []
        steps += 1
        grid[r][c] = str(graph_id)

        if (
            c + 1 < len(grid[0])
            and grid[r][c + 1] != "#"
            and not grid[r][c + 1].isnumeric()
        ):
            nexts.append((r, c + 1))

        if c - 1 > -1 and grid[r][c - 1] != "#" and not grid[r][c - 1].isnumeric():
            nexts.append((r, c - 1))

        if r - 1 > -1 and grid[r - 1][c] != "#" and not grid[r - 1][c].isnumeric():
            nexts.append((r - 1, c))

        if (
            r + 1 < len(grid)
            and grid[r + 1][c] != "#"
            and not grid[r + 1][c].isnumeric()
        ):
            nexts.append((r + 1, c))

        if len(nexts) != 1:
            break

        else:
            r, c = nexts[0]

    stepsd[graph_id] = steps - 1

    intersection = next(id_gen)
    grid[r][c] = str(intersection)
    stepsd[intersection] = 1

    maze_graph[graph_id].add(intersection)
    maze_graph[intersection].add(graph_id)

    for nxt in nexts:
        if grid[nxt[0]][nxt[1]].isnumeric():
            next_id = int(grid[nxt[0]][nxt[1]])
            maze_graph[intersection].add(next_id)
            maze_graph[next_id].add(intersection)

        else:
            next_id = next(id_gen)
            maze_graph[intersection].add(next_id)
            maze_graph[next_id].add(intersection)
            convert_maze_to_graph(*nxt, next_id)


convert_maze_to_graph(*start, next(id_gen))

max_ = [0]


def dfs(node, path, steps):
    steps += stepsd[node]
    if node == end[0]:
        max_[0] = max(max_[0], steps)
        return

    path.add(node)

    for neighbour in maze_graph[node]:
        if neighbour not in path:
            dfs(neighbour, path, steps)

    path.remove(node)


dfs(0, set(), 0)

open("day23-p2-output.txt", "w").write(str(max_[0]))
