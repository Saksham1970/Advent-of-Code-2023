from functools import cache
from scipy.interpolate import interp1d

with open("day21-p1-input.txt", "r") as f:
    grid = [list(i.strip()) for i in f.readlines()]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start = (i, j)
            grid[i][j] = "."

end_points = set()


@cache
def dfs(i, j, steps):
    if steps == 0:
        end_points.add((i, j))
        return

    for d in {1, -1}:
        i_d = (i + d) % len(grid)
        i_ = i % len(grid)
        j_d = (j + d) % len(grid[0])
        j_ = j % len(grid[0])

        if grid[i_d][j_] == ".":
            dfs(i + d, j, steps - 1)
        if grid[i_][j_d] == ".":
            dfs(i, j + d, steps - 1)


def res_less(x):
    global end_points
    dfs.cache_clear()
    end_points = set()
    dfs(*start, x)
    return len(end_points)


def res(x):
    if x < 3 * len(grid):
        return res_less(x)
    else:
        a = x % len(grid)
        req = x // len(grid)
        nums = [res_less(a), res_less(a + len(grid)), res_less(a + 2 * len(grid))]
        interp = interp1d([0, 1, 2], nums, kind="quadratic", fill_value="extrapolate")
        return int(interp(req))


open("day21-p1-output.txt", "w").write(str(res(64)))
open("day21-p2-output.txt", "w").write(str(res(26501365)))
