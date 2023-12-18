from functools import cache

with open("day12-p1-input.txt", "r") as f:
    input_ = [i.strip().replace(",", " ").split() for i in f.readlines()]

for i in range(len(input_)):
    input_[i] = [input_[i][0], input_[i][1:]]
    input_[i][1] = tuple([int(j) for j in input_[i][1]])

    input_[i][0] = ((input_[i][0] + "?") * 5)[:-1]
    input_[i][1] = input_[i][1] * 5


@cache
def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)

    if cfg[0] in "#?":
        if (
            nums[0] <= len(cfg)
            and "." not in cfg[: nums[0]]
            and (nums[0] == len(cfg) or cfg[nums[0]] != "#")
        ):
            result += count(cfg[nums[0] + 1 :], nums[1:])

    return result


total = 0

for cfg, nums in input_:
    total += count(cfg, nums)

with open("day12-p2-output.txt", "w") as f:
    f.write(str(total))
