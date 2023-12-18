patterns = []
pattern = []
with open("day13-p1-input.txt", "r") as f:
    for line in f:
        if line.strip() != "":
            pattern.append(list(line.strip()))
        else:
            patterns.append(pattern)
            pattern = []
    patterns.append(pattern)


res = 0
lines = []
for pattern in patterns:
    horis = set(list(range(len(pattern) - 1)))
    verts = set(list(range(len(pattern[0]) - 1)))

    for i in range(len(pattern) - 1):
        for j in range(len(pattern[0])):
            if i in horis and pattern[i][j] != pattern[i + 1][j]:
                horis.remove(i)

    for j in range(len(pattern[0]) - 1):
        for i in range(len(pattern)):
            if j in verts and pattern[i][j] != pattern[i][j + 1]:
                verts.remove(j)

    # Here horis has possible horizontal lines of reflections, and verts has vertical ones

    for hori in horis:
        part1 = pattern[: hori + 1][::-1]
        part2 = pattern[hori + 1 :]
        for i in range(min(len(part1), len(part2))):
            if part1[i] != part2[i]:
                break
        else:
            res += (hori + 1) * 100
            horis.remove(hori)
            break

    else:
        pattern_transpose = [[0] * len(pattern) for _ in range(len(pattern[0]))]
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                pattern_transpose[j][i] = pattern[i][j]

        for vert in verts:
            part1 = pattern_transpose[: vert + 1][::-1]
            part2 = pattern_transpose[vert + 1 :]
            for i in range(min(len(part1), len(part2))):
                if part1[i] != part2[i]:
                    break
            else:
                res += vert + 1
                verts.remove(vert)
                break

    lines.append([horis, verts])

with open("day13-p1-output.txt", "w") as f:
    f.write(str(res))


res = 0

for ind, pattern in enumerate(patterns):
    horis, verts = lines[ind]

    for hori in horis:
        part1 = pattern[: hori + 1][::-1]
        part2 = pattern[hori + 1 :]
        mismatch = 0
        for i in range(min(len(part1), len(part2))):
            for j in range(len(pattern[0])):
                if part1[i][j] != part2[i][j]:
                    mismatch += 1

        if mismatch == 1:
            res += (hori + 1) * 100
            break

    else:
        horis = set()
        pattern_transpose = [[0] * len(pattern) for _ in range(len(pattern[0]))]
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                pattern_transpose[j][i] = pattern[i][j]

        for vert in verts:
            part1 = pattern_transpose[: vert + 1][::-1]
            part2 = pattern_transpose[vert + 1 :]
            mismatch = 0
            for i in range(min(len(part1), len(part2))):
                for j in range(len(pattern)):
                    if part1[i][j] != part2[i][j]:
                        mismatch += 1

            if mismatch == 1:
                res += vert + 1
                break
        else:
            verts = set()

            for i in range(len(pattern) - 1):
                mismatch = 0
                for j in range(len(pattern[0])):
                    if pattern[i][j] != pattern[i + 1][j]:
                        mismatch += 1

                if mismatch == 1:
                    horis.add(i)

            for j in range(len(pattern[0]) - 1):
                mismatch = 0
                for i in range(len(pattern)):
                    if pattern[i][j] != pattern[i][j + 1]:
                        mismatch += 1
                if mismatch == 1:
                    verts.add(j)

            for hori in horis:
                part1 = pattern[: hori + 1][::-1]
                part2 = pattern[hori + 1 :]
                mismatch = 0
                for i in range(min(len(part1), len(part2))):
                    for j in range(len(pattern[0])):
                        if part1[i][j] != part2[i][j]:
                            mismatch += 1
                if mismatch == 1:
                    res += (hori + 1) * 100
                    break

            else:
                pattern_transpose = [[0] * len(pattern) for _ in range(len(pattern[0]))]
                for i in range(len(pattern)):
                    for j in range(len(pattern[0])):
                        pattern_transpose[j][i] = pattern[i][j]

                for vert in verts:
                    part1 = pattern_transpose[: vert + 1][::-1]
                    part2 = pattern_transpose[vert + 1 :]
                    mismatch = 0
                    for i in range(min(len(part1), len(part2))):
                        for j in range(len(pattern)):
                            if part1[i][j] != part2[i][j]:
                                mismatch += 1

                    if mismatch == 1:
                        res += vert + 1
                        break

with open("day13-p2-output.txt", "w") as f:
    f.write(str(res))
