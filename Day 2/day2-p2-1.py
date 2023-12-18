import pickle
from functools import reduce

with open("day2-p1-intermediate.obj", "rb") as f:
    games = pickle.load(f)


res = 0
for game in games:
    minimum_set = [0, 0, 0]
    for outcome in games[game]:
        for i in range(3):
            minimum_set[i] = max(minimum_set[i], outcome[i])

    res += reduce(lambda a, b: a * b, minimum_set)

with open("day2-p2-output.txt", "w") as f:
    f.write(str(res))
