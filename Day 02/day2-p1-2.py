import pickle

with open("day2-p1-intermediate.obj", "rb") as f:
    games = pickle.load(f)


target = (12, 13, 14)

res = 0

for game in games:
    for outcome in games[game]:
        for i in range(3):
            if outcome[i] > target[i]:
                break
        else:
            continue
        break
    else:
        res += game

with open("day2-p1-output.txt", "w") as f:
    f.write(str(res))
