from collections import defaultdict
import pickle


cards = defaultdict(list)

with open("day4-p1-input.txt", "r") as f:
    for line in f:
        line = line.replace(":", " :")
        line = line.split()

        nums = []
        card_no = None

        for word in line:
            if word.isnumeric():
                if not card_no:
                    card_no = int(word)
                else:
                    nums.append(int(word))

            elif word == "|":
                cards[card_no].append(nums)
                nums = []
        cards[card_no].append(nums)


with open("day4-p1-intermediate.obj", "wb") as f:
    pickle.dump(cards, f)
