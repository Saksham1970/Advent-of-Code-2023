from collections import OrderedDict

boxes = [OrderedDict() for i in range(256)]

with open("day15-p1-input.txt", "r") as f:
    input_ = f.readline().strip().split(",")


def hash(s):
    current_val = 0
    for c in s:
        current_val += ord(c)
        current_val *= 17
        current_val = current_val % 256
    return current_val


for inp in input_:
    if inp[-1] == "-":
        label = inp[:-1]
        box = hash(label)
        if label in boxes[box]:
            boxes[box].pop(label)
    else:
        label = inp[:-2]
        box = hash(label)
        focal_length = int(inp[-1])
        boxes[box][label] = focal_length

res = 0
for i, box in enumerate(boxes):
    for j, label in enumerate(box):
        res += (i + 1) * (j + 1) * box[label]

with open("day15-p2-output.txt", "w") as f:
    f.write(str(res))
