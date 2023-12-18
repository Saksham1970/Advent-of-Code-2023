from math import floor, ceil
from functools import reduce

times = [53717880]
dists = [275118112151524]

# Quadratic Formula
dets = [(times[i] ** 2 - 4 * dists[i]) ** 0.5 for i in range(len(times))]
mins = [ceil((times[i] - dets[i]) / 2) for i in range(len(times))]
maxs = [floor((times[i] + dets[i]) / 2) for i in range(len(times))]

ways = [maxs[i] - mins[i] + 1 for i in range(len(maxs))]
print(reduce(lambda a, b: a * b, ways))
