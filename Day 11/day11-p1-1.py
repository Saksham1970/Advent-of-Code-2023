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

for i in range(len(grid)):
    offset = 0
    for col in empty_cols:
        grid[i].insert(col + offset, ".")
        offset += 1

offset = 0
for row in empty_rows:
    grid.insert(row + offset, ["."] * (len(grid[0])))
    offset += 1


galaxies = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            galaxies.append((i, j))

sum_ = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        sum_ += abs(galaxies[i][0] - galaxies[j][0])
        sum_ += abs(galaxies[i][1] - galaxies[j][1])


with open("day11-p1-output.txt", "w") as f:
    f.write(str(sum_))
