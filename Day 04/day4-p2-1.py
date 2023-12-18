import pickle

with open("day4-p1-intermediate.obj", "rb") as f:
    cards = pickle.load(f)

# DP keeps the amount of cards stored
dp = [1] * len(cards)

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

    i = card
    while matches > 0 and i < len(dp):
        dp[i] += dp[card - 1]
        matches -= 1
        i += 1

with open("day4-p2-output.txt", "w") as f:
    f.write(str(sum(dp)))
