import modules

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
i = 0

while i < 1000:
    modules.pulses[0] += 1
    modules.modules["broadcaster"].recieve_pulse(False, "button")
    modules.process()
    i += 1

open("day20-p1-output.txt", "w").write(str(modules.pulses[0] * modules.pulses[1]))
