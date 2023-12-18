import pickle
from pprint import pprint

with open("day5-p1-intermediate.obj", "rb") as f:
    maps = pickle.load(f)

seeds = maps[0][0]
maps.pop(0)

seeds_range = []
i = 0
while i < len(seeds):
    seeds_range.append([seeds[i], seeds[i + 1]])
    i += 2

for map in maps:
    map.sort(key=lambda x: x[1])

new_range = []
for map in maps:
    i = 0
    while i < len(seeds_range):
        for destination, source, offset in map:
            if source <= seeds_range[i][0]:
                if source + offset > seeds_range[i][0]:
                    if source + offset > seeds_range[i][0] + seeds_range[i][1] - 1:
                        # if the source range is fully in the available range

                        new_range.append(
                            [
                                destination + seeds_range[i][0] - source,
                                seeds_range[i][1],
                            ]
                        )
                    else:
                        # if the source range is not fully in the available range, cut the range

                        new_range.append(
                            [
                                destination + seeds_range[i][0] - source,
                                offset - seeds_range[i][0] + source,
                            ]
                        )
                        seeds_range.insert(
                            i + 1,
                            [
                                source + offset,
                                seeds_range[i][0] + seeds_range[i][1] - source - offset,
                            ],
                        )
            else:
                break
        i += 1
    seeds_range = new_range
    new_range = []

with open("day5-p2-output.txt", "w") as f:
    f.write(str(min(seeds_range, key=lambda x: x[0])[0]))
