directions_map = {"U": 3, "L": 2, "D": 1, "R": 0}

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open("day18-p1-input.txt", "r") as f:
    input_ = [i.strip().split() for i in f.readlines()]

input_ = list(map(lambda tup: (tup[0], int(tup[1]), tup[2][2:-1]), input_))

coords = set()
r, c = 0, 0
max_r, max_c = 0, 0
min_r, min_c = 0, 0

for direction, amount, _ in input_:
    dr, dc = directions[directions_map[direction]]
    for i in range(amount):
        r, c = r + dr, c + dc

        max_r, max_c, min_r, min_c = (
            max(r, max_r),
            max(c, max_c),
            min(r, min_r),
            min(c, min_c),
        )

        if i == amount - 1:
            direction = "C"
        coords.add((r, c, direction))

MAX_R, MAX_C = max_r - min_r, max_c - min_c

grid = [["."] * (MAX_C + 1) for _ in range(MAX_R + 1)]

for r, c, direction in coords:
    grid[r - min_r][c - min_c] = direction


insides = 0
for r, row in enumerate(grid):
    current_count = 0
    inside = False
    for c, char in enumerate(row):
        if char == "U":
            inside = True

        elif char == "D":
            inside = False
            insides += current_count
            current_count = 0

        elif char == "." and inside:
            current_count += 1

        elif char == "C":
            if (r > 0 and grid[r - 1][c] == "U") or (
                r < len(grid) - 1 and grid[r + 1][c] == "U"
            ):
                inside = True
            else:
                inside = False
                insides += current_count
                current_count = 0

with open("day18-p1-output.txt", "w") as f:
    f.write(str(insides + len(coords)))
