import heapq
from collections import defaultdict


def type_(hand):
    count = defaultdict(int)
    for c in hand:
        count[c] += 1

    counts = []
    for c in count:
        counts.append(-count[c])
    heapq.heapify(counts)

    first = heapq.heappop(counts)

    if first == -5:
        return 6
    elif first == -4:
        return 5
    elif first == -3:
        second = heapq.heappop(counts)
        if second == -2:
            return 4
        else:
            return 3
    elif first == -2:
        second = heapq.heappop(counts)
        if second == -2:
            return 2
        else:
            return 1
    else:
        return 0


heap = []
with open("day7-p1-input.txt", "r") as f:
    for line in f:
        line = line.split()
        line[0] = line[0].replace("A", "Z").replace("T", "B").replace("K", "Y")
        heap.append((type_(line[0]), line[0], int(line[1])))
heapq.heapify(heap)

res = 0
rank = 1
while heap:
    _, _, value = heapq.heappop(heap)
    res += rank * value
    rank += 1

with open("day7-p1-output.txt", "w") as f:
    f.write(str(res))
