from functools import reduce

graph = {}


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a // gcd(a, b)) * b


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


steps_d = {}

for node in graph:
    if node[-1] == "A":
        curr = node
        i = 0
        steps = 0
        while True:
            direction = route[i]
            if direction == "L":
                curr = graph[curr][0]
            else:
                curr = graph[curr][1]
            steps += 1
            i = (i + 1) % (len(route))

            if curr[-1] == "Z":
                steps_d[node] = steps
                break


final_value = reduce(lcm, list(steps_d.values()))

with open("day8-p2-output.txt", "w") as f:
    f.write(str(final_value))
