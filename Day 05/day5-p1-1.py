import pickle

maps = []

with open("day5-p1-input.txt", "r") as f:
    current_category = []
    for line in f:
        if line == "\n":
            maps.append(current_category)
            current_category = []
        elif line[-2] == ":":
            continue
        else:
            current_category.append([int(x) for x in line.split()])
    maps.append(current_category)

with open("day5-p1-intermediate.obj", "wb") as f:
    pickle.dump(maps, f)
