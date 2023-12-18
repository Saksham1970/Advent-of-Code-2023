directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open("day18-p1-input.txt", "r") as f:
    input_ = [i.strip().split()[2][2:-1] for i in f.readlines()]

input_ = list(map(lambda x: (int(x[-1]), int(x[:-1], 16)), input_))


def calc_points(points, boundary):
    """
    ? Shoelace Formula and Pick Theorem used
    https://en.wikipedia.org/wiki/Shoelace_formula
    https://en.wikipedia.org/wiki/Pick%27s_theorem
    """

    # ? Shoelace Formula for area given vertices
    A = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        A += (x1 * y2 - x2 * y1) / 2

    A = int(abs(A))

    # ? Pick Theorem: A = i + b/2 - 1
    # ? i + b = total points = A + b/2 + 1

    return A + boundary // 2 + 1


r, c = 0, 0

points = [(r, c)]
boundary = 0

for direction, amount in input_:
    dr, dc = directions[direction]
    r, c = r + dr * amount, c + dc * amount
    boundary += amount
    points.append((r, c))


with open("day18-p2-output.txt", "w") as f:
    f.write(str(calc_points(points, boundary)))
