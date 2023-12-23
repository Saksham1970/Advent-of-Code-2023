import sys

sys.setrecursionlimit(5000)

with open("day23-input.txt", "r") as f:
    grid = [list(i.strip()) for i in f.readlines()]

for j in range(len(grid[0])):
    if grid[0][j] == ".":
        start = (0, j)

max_ = [0]


def dfs(r, c, steps):
    if r == len(grid) - 1:
        max_[0] = max(max_[0], steps)
        return

    char = grid[r][c]

    grid[r][c] = "#"

    if char == "." or char == ">":
        if c + 1 < len(grid[0]) and grid[r][c + 1] != "#":
            dfs(r, c + 1, steps + 1)
    if char == "." or char == "<":
        if c - 1 > -1 and grid[r][c - 1] != "#":
            dfs(r, c - 1, steps + 1)
    if char == "." or char == "^":
        if r - 1 > -1 and grid[r - 1][c] != "#":
            dfs(r - 1, c, steps + 1)

    if char == "." or char == "v":
        if r + 1 < len(grid) and grid[r + 1][c] != "#":
            dfs(r + 1, c, steps + 1)

    grid[r][c] = char


dfs(*start, 0)

open("day23-p1-output.txt", "w").write(str(max_[0]))
