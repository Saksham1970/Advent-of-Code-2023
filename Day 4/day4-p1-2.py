import pickle

with open("day4-p1-intermediate.obj", "rb") as f:
    cards = pickle.load(f)

res = 0
for card in cards:
    winning, have = cards[card]
    winning.sort()
    have.sort()

    i = 0
    j = 0
    matches = 0
    while i < len(winning) and j < len(have):
        if winning[i] > have[j]:
            j += 1
        elif winning[i] < have[j]:
            i += 1
        else:
            i += 1
            j += 1
            matches += 1

    res += int(2 ** (matches - 1))

with open("day4-p1-output.txt", "w") as f:
    f.write(str(res))
