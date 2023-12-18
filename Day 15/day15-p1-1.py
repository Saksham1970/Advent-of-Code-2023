with open("day15-p1-input.txt", "r") as f:
    input_ = f.readline().strip().split(",")


def hash(s):
    current_val = 0
    for c in s:
        current_val += ord(c)
        current_val *= 17
        current_val = current_val % 256
    return current_val


with open("day15-p1-output.txt", "w") as f:
    f.write(str(sum([hash(i) for i in input_])))
