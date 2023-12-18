with open("day11-p1-input.txt", "r") as f:
    grid = [list(i.strip()) for i in f.readlines()]

empty_rows = set(list(range(len(grid))))
empty_cols = set(list(range(len(grid[0]))))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            if i in empty_rows:
                empty_rows.remove(i)
            if j in empty_cols:
                empty_cols.remove(j)

empty_rows = list(empty_rows)
empty_rows.sort()
empty_cols = list(empty_cols)
empty_cols.sort()

expansion_ratio = 1000000

galaxies = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            count_c = 0
            count_r = 0

            for c in empty_cols:
                if c > j:
                    break
                count_c += 1

            for r in empty_rows:
                if r > i:
                    break
                count_r += 1

            galaxies.append(
                (
                    i + count_r * (expansion_ratio - 1),
                    j + count_c * (expansion_ratio - 1),
                )
            )

sum_ = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        sum_ += abs(galaxies[i][0] - galaxies[j][0])
        sum_ += abs(galaxies[i][1] - galaxies[j][1])

with open("day11-p2-output.txt", "w") as f:
    f.write(str(sum_))
