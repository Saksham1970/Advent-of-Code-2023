import modules
from collections import defaultdict
from math import lcm

names = []
links = []

with open("day20-p1-input.txt", "r") as f:
    for line in f:
        name, link = line.strip().split("->")
        name = name.strip()
        link = [i.strip() for i in link.split(",")]
        names.append(name)
        links.append(link)

modules.add_modules(names, links)
penultimate = list(modules.modules["rx"].inputs)[0]
antipenultimates = list(modules.modules[penultimate].inputs)
ap_cycles = defaultdict(list)

i = 0
while True:
    i += 1
    modules.pulses[0] += 1
    modules.modules["broadcaster"].recieve_pulse(False, "button")
    name = modules.process(antipenultimates)
    if name:
        ap_cycles[name].append(i)
        if len(ap_cycles) == len(antipenultimates):
            break

open("day20-p2-output.txt", "w").write(str(lcm(*[i[0] for i in ap_cycles.values()])))
