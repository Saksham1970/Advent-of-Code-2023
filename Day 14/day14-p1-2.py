dirs = [-1 + 0j, 0 - 1j, 1 + 0j, 0 + 1j]

with open("day14-p1-input.txt", "r") as f:
    grid = [list(i.strip()) for i in f.readlines()]

pebbles = []

cycle = {}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            pebbles.append(complex(i, j))

frozen_pebbles = frozenset(pebbles)
cyc_no = 1
while True:
    for dir in range(4):
        match dir:
            case 0:
                pebbles.sort(key=lambda x: x.real)
            case 2:
                pebbles.sort(key=lambda x: x.real, reverse=True)
            case 1:
                pebbles.sort(key=lambda x: x.imag)
            case 3:
                pebbles.sort(key=lambda x: x.imag, reverse=True)

        offset = dirs[dir]
        for i in range(len(pebbles)):
            pebble = pebbles.pop(i)
            grid[int(pebble.real)][int(pebble.imag)] = "."
            next = pebble
            while True:
                if (
                    next.real < 0
                    or next.imag < 0
                    or next.real > len(grid) - 1
                    or next.imag > len(grid[0]) - 1
                    or grid[int(next.real)][int(next.imag)] == "#"
                    or grid[int(next.real)][int(next.imag)] == "O"
                ):
                    break

                pebble = next
                next += offset

            grid[int(pebble.real)][int(pebble.imag)] = "O"
            pebbles.insert(i, pebble)

    frozen_pebbles = frozenset(pebbles)
    if frozen_pebbles in cycle:
        transient = cycle[frozen_pebbles]
        break
    else:
        cycle[frozen_pebbles] = cyc_no
        cyc_no += 1


loads = {}
for cyc in cycle:
    if cycle[cyc] >= transient:
        loads[cycle[cyc]] = cyc

period = len(loads)


def load(pebbles):
    sum_ = 0
    for pebble in pebbles:
        sum_ += len(grid) - pebble.real
    return int(sum_)


with open("day14-p2-output.txt", "w") as f:
    f.write(str(load(loads[(1_000_000_000 - transient) % period + transient])))
