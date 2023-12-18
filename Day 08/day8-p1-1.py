graph = {}

with open("day8-p1-input.txt", "r") as f:
    route = f.readline()[:-1]
    f.readline()
    for line in f:
        source, left, right = (
            line.replace("= ", "")
            .replace("(", "")
            .replace(")", "")
            .replace(",", "")
            .split()
        )
        graph[source] = [left, right]

curr = "AAA"
i = 0
steps = 0
while curr != "ZZZ":
    direction = route[i]
    if direction == "L":
        curr = graph[curr][0]
    else:
        curr = graph[curr][1]
    steps += 1
    i = (i + 1) % (len(route))

with open("day8-p1-output.txt", "w") as f:
    f.write(str(steps))
