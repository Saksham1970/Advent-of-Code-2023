import heapq

board = {
    (i, j): int(c)
    for i, r in enumerate(open("day17-input.txt"))
    for j, c in enumerate(r.strip())
}


def minimal_heat(start, end, least, most):
    queue = [(0, *start, 0, 0)]
    seen = set()
    while queue:
        heat, x, y, prev_dx, prev_dy = heapq.heappop(queue)
        if (x, y) == end:
            return heat
        if (x, y, prev_dx, prev_dy) in seen:
            continue

        seen.add((x, y, prev_dx, prev_dy))

        # calculate turns only
        for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)} - {
            (prev_dx, prev_dy),
            (-prev_dx, -prev_dy),
        }:
            curr_x, curr_y, curr_heat = x, y, heat
            for i in range(1, most + 1):
                curr_x, curr_y = curr_x + dx, curr_y + dy
                if (curr_x, curr_y) in board:
                    curr_heat += board[curr_x, curr_y]
                    if i >= least:
                        heapq.heappush(queue, (curr_heat, curr_x, curr_y, dx, dy))


with open("day17-p1-output.txt", "w") as f:
    f.write(str(minimal_heat((0, 0), max(board), 1, 3)))
with open("day17-p2-output.txt", "w") as f:
    f.write(str(minimal_heat((0, 0), max(board), 4, 10)))
