import pickle

with open("day5-p1-intermediate.obj", "rb") as f:
    maps = pickle.load(f)

seeds = maps[0][0]
maps.pop(0)

# kepps all the conversions in it
seed_table = [seeds]

for map in maps:
    map.sort(key=lambda x: x[1])


for map in maps:
    curr = seed_table[-1]
    seed_table.append(curr[:])

    for i in range(len(curr)):
        for destination, source, offset in map:
            # print(source, curr[i])
            if source <= curr[i]:
                if source + offset > curr[i]:
                    seed_table[-1][i] = destination + curr[i] - source
            else:
                break

min_j = 0
for j in range(len(seed_table[-1])):
    if seed_table[-1][j] < seed_table[-1][min_j]:
        min_j = j

with open("day5-p1-output.txt", "w") as f:
    f.write(str(seed_table[-1][min_j]))
