with open("day10-p1-input.txt", "r") as f:
    grid = [list(i.strip()) for i in f.readlines()]

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


def find_loop(i, j, direction):
    path = set()

    while True:
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
            return set()

        if grid[i][j] == "S":
            path.add((i, j))
            return path

        next_i, next_j, next_direction = i, j, direction

        if direction == UP:
            if grid[i][j] == "|":
                next_i = i - 1
                next_direction = UP
            elif grid[i][j] == "7":
                next_j = j - 1
                next_direction = LEFT
            elif grid[i][j] == "F":
                next_j = j + 1
                next_direction = RIGHT

        elif direction == DOWN:
            if grid[i][j] == "|":
                next_i = i + 1
                next_direction = DOWN
            elif grid[i][j] == "J":
                next_j = j - 1
                next_direction = LEFT
            elif grid[i][j] == "L":
                next_j = j + 1
                next_direction = RIGHT

        elif direction == LEFT:
            if grid[i][j] == "-":
                next_j = j - 1
                next_direction = LEFT
            elif grid[i][j] == "L":
                next_i = i - 1
                next_direction = UP
            elif grid[i][j] == "F":
                next_i = i + 1
                next_direction = DOWN

        elif direction == RIGHT:
            if grid[i][j] == "-":
                next_j = j + 1
                next_direction = RIGHT
            elif grid[i][j] == "7":
                next_i = i + 1
                next_direction = DOWN
            elif grid[i][j] == "J":
                next_i = i - 1
                next_direction = UP

        if next_direction == direction and next_i == i and next_j == j:
            return set()

        path.add((i, j))
        i, j, direction = next_i, next_j, next_direction


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start = (i, j)
            break

if len(path := find_loop(start[0], start[1] + 1, RIGHT)) > 0:
    pass
elif len(path := find_loop(start[0], start[1] - 1, LEFT)) > 0:
    pass
elif len(path := find_loop(start[0] - 1, start[1], UP)) > 0:
    pass
elif len(path := find_loop(start[0] + 1, start[1], DOWN)) > 0:
    pass


with open("day10-p1-output.txt", "w") as f:
    f.write(str(len(path) // 2))

area = 0

for r, row in enumerate(grid):
    inside = False

    for c, cell in enumerate(row):
        if (r, c) not in path:
            area += inside
        else:
            inside = inside ^ (cell in "|F7")


with open("day10-p2-output.txt", "w") as f:
    f.write(str(area))
