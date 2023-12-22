from collections import defaultdict

with open("day22-input.txt", "r") as f:
    bricks = [
        list(map(lambda x: tuple(map(int, x.split(","))), i.strip().split("~")))
        for i in f.readlines()
    ]

for i in range(len(bricks)):
    if bricks[i][0][0] != bricks[i][1][0]:
        rotation = 0
    elif bricks[i][0][1] != bricks[i][1][1]:
        rotation = 1
    else:
        rotation = 2
    bricks[i].sort(key=lambda x: x[rotation])
    bricks[i].append(rotation)

bricks.sort(key=lambda x: x[0][2])

topdown = [[(0, -1)] * 10 for _ in range(10)]
supported_by = defaultdict(set)
dependent_on = defaultdict(set)

for i, (start, end, rotation) in enumerate(bricks):
    # Vertical Case
    if rotation == 2:
        height = end[2] - start[2] + 1
        x, y = start[0], start[1]

        curr_h, curr_brick = topdown[x][y]

        if curr_brick != -1:
            supported_by[curr_brick].add(i)
            dependent_on[i].add(curr_brick)

        topdown[x][y] = (curr_h + height, i)

    # Horizontal Cases
    else:
        x, y, _ = start
        max_ = 0
        for j in range(start[rotation], end[rotation] + 1):
            if rotation == 0:
                x = j
            else:
                y = j

            max_ = max(max_, topdown[x][y][0])

        for j in range(start[rotation], end[rotation] + 1):
            if rotation == 0:
                x = j
            else:
                y = j

            if topdown[x][y][0] == max_ and topdown[x][y][1] != -1:
                supported_by[topdown[x][y][1]].add(i)
                dependent_on[i].add(topdown[x][y][1])

        for j in range(start[rotation], end[rotation] + 1):
            if rotation == 0:
                x = j
            else:
                y = j

            topdown[x][y] = (max_ + 1, i)

res = 0
for i in range(len(bricks)):
    if i not in supported_by:
        res += 1
        continue

    for dependend in supported_by[i]:
        if len(dependent_on[dependend]) == 1:
            break
    else:
        res += 1

open("day22-p1-output.txt", "w").write(str(res))

fell = set()


def fall(i):
    if i not in supported_by:
        return 0

    fallen = 0
    fell.add(i)

    for dependend in supported_by[i]:
        if dependent_on[dependend].issubset(fell):
            fallen += 1 + fall(dependend)

    return fallen


res = 0
for i in range(len(bricks)):
    res += fall(i)
    fell = set()

open("day22-p2-output.txt", "w").write(str(res))
