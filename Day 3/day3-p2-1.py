with open("day3-p1-preprocess.txt", "r") as f:
    grid = f.readlines()
    grid = [list(a) for a in grid]

res = 0
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != "*":
            continue

        coord_set = set()

        for search_r in [r - 1, r, r + 1]:
            for search_c in [c - 1, c, c + 1]:
                if (
                    search_r < 0
                    or search_r >= len(grid)
                    or search_c < 0
                    or search_c >= len(grid[search_r])
                    or not grid[search_r][search_c].isnumeric()
                ):
                    continue
                while search_c > 0 and grid[search_r][search_c - 1].isnumeric():
                    search_c -= 1
                coord_set.add((search_r, search_c))

        if len(coord_set) != 2:
            continue

        gear_ratio = 1
        for i, j in coord_set:
            curr = grid[i]
            k = j
            while k < len(curr) and curr[k].isnumeric():
                k += 1
            gear_ratio *= int("".join(curr[j:k]))

        res += gear_ratio

with open("day3-p2-output.txt", "w") as f:
    f.write(str(res))
