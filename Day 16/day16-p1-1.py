from copy import deepcopy

with open("day16-p1-input.txt", "r") as f:
    grid = [list(i.strip()) for i in f.readlines()]

visited = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


def travel(i, j, direction, visited):
    while True:
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
            return

        if direction in visited[i][j]:
            return

        next_i, next_j, next_direction = i, j, direction

        if direction == UP:
            if grid[i][j] == "." or grid[i][j] == "|":
                next_i = i - 1
                next_direction = UP
            elif grid[i][j] == "\\":
                next_j = j - 1
                next_direction = LEFT
            elif grid[i][j] == "/":
                next_j = j + 1
                next_direction = RIGHT
            else:
                next_j = j + 1
                next_direction = RIGHT
                visited[i][j].append(direction)
                travel(i, j - 1, LEFT, visited)

        elif direction == DOWN:
            if grid[i][j] == "|" or grid[i][j] == ".":
                next_i = i + 1
                next_direction = DOWN
            elif grid[i][j] == "/":
                next_j = j - 1
                next_direction = LEFT
            elif grid[i][j] == "\\":
                next_j = j + 1
                next_direction = RIGHT
            else:
                next_j = j + 1
                next_direction = RIGHT
                visited[i][j].append(direction)
                travel(i, j - 1, LEFT, visited)

        elif direction == LEFT:
            if grid[i][j] == "-" or grid[i][j] == ".":
                next_j = j - 1
                next_direction = LEFT
            elif grid[i][j] == "\\":
                next_i = i - 1
                next_direction = UP
            elif grid[i][j] == "/":
                next_i = i + 1
                next_direction = DOWN
            else:
                next_i = i - 1
                next_direction = UP
                visited[i][j].append(direction)
                travel(i + 1, j, DOWN, visited)

        elif direction == RIGHT:
            if grid[i][j] == "-" or grid[i][j] == ".":
                next_j = j + 1
                next_direction = RIGHT
            elif grid[i][j] == "\\":
                next_i = i + 1
                next_direction = DOWN
            elif grid[i][j] == "/":
                next_i = i - 1
                next_direction = UP
            else:
                next_i = i - 1
                next_direction = UP
                visited[i][j].append(direction)
                travel(i + 1, j, DOWN, visited)

        if direction not in visited[i][j]:
            visited[i][j].append(direction)

        i, j, direction = next_i, next_j, next_direction


def helper(i, j, direction):
    temp_visited = deepcopy(visited)
    travel(i, j, direction, temp_visited)

    res = 0
    for row in temp_visited:
        res += row.count([])
    res = len(grid) * len(grid[0]) - res

    return res


res = helper(0, 0, RIGHT)

with open("day16-p1-output.txt", "w") as f:
    f.write(str(res))

max_ = res

for i in range(len(grid)):
    max_ = max(max_, helper(i, 0, RIGHT), helper(i, len(grid[0]) - 1, LEFT))

for j in range(len(grid[0])):
    max_ = max(max_, helper(0, j, DOWN), helper(len(grid) - 1, j, UP))

with open("day16-p2-output.txt", "w") as f:
    f.write(str(max_))
