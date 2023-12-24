from sympy import Point, Line
import numpy as np

lines = {}
lines_list = []

test_min = 200000000000000
test_max = 400000000000000


with open("day24-input.txt", "r") as f:
    for i in f.readlines():
        position, velocity = i.strip().split("@")
        position, velocity = list(map(int, position.split(","))), list(
            map(int, velocity.split(","))
        )

        p1, p2 = Point(*position[:2], evaluate=True), Point(
            *velocity[:2], evaluate=True
        )
        l1 = Line(p1, p1 + p2)
        lines[l1] = [
            np.array(p1.coordinates, dtype=np.float64),
            np.array(p2.coordinates, dtype=np.float64),
        ]
        lines_list.append(l1)


res = 0
for i in range(len(lines_list) - 1):
    for j in range(i + 1, len(lines_list)):
        intersection = lines_list[i].intersection(lines_list[j])
        if not intersection:
            continue
        intersection = intersection[0].evalf()
        intersection = np.array(intersection, dtype=np.float64)

        if np.all(np.logical_and(intersection >= test_min, intersection <= test_max)):
            if (
                (
                    (intersection - lines[lines_list[i]][0]) / lines[lines_list[i]][1]
                    > 0
                )[0]
            ) and (
                (
                    (intersection - lines[lines_list[j]][0]) / lines[lines_list[j]][1]
                    > 0
                )[0]
            ):
                res += 1

open("day24-p1-output.txt", "w").write(str(res))
