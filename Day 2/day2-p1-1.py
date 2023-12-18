from collections import defaultdict
import pickle

# Preprocess input into intermediate dictionary object

game = defaultdict(list)

with open("day2-p1-input.txt", "r") as f:
    for line in f:
        line = line.replace(",", " ,")
        line = line.replace(";", " ;")
        line = line.replace(":", " :")
        line = line.split()

        line[1] = int(line[1])

        state = [0, 0, 0]
        for i in range(2, len(line)):
            if line[i].isnumeric():
                if line[i + 1] == "red":
                    state[0] = int(line[i])

                elif line[i + 1] == "green":
                    state[1] = int(line[i])

                if line[i + 1] == "blue":
                    state[2] = int(line[i])

            if line[i] == ";":
                game[line[1]].append(tuple(state))
                state = [0, 0, 0]

        game[line[1]].append(tuple(state))
        state = [0, 0, 0]

with open("day2-p1-intermediate.obj", "wb") as f:
    pickle.dump(game, f)
