from collections import deque

pulse_sequence = deque()
modules = {}
pulses = [0, 0]


class Module:
    def __init__(self, name):
        self.name = name
        self.links = []
        self.state = None
        self.inputs = set()

    def add_links(self, links):
        self.links = links

    def pulse_links(self, pulse):
        # print(self.name + " pulsing ", pulse)

        pulses[int(pulse)] += len(self.links)

        for link in self.links:
            pulse_sequence.append((link, pulse, self.name))

    def recieve_pulse(self, pulse, name):
        NotImplemented

    def add_input(self, link):
        self.inputs.add(link)


class FlipFlops(Module):
    def __init__(self, name):
        super().__init__(name)
        self.state = False

    def recieve_pulse(self, pulse, name):
        if not pulse:
            self.state = not self.state
            self.pulse_links(self.state)


class Conjuction(Module):
    def __init__(self, name):
        super().__init__(name)
        self.memories = {}
        self.false_counts = 0

    def add_input(self, link):
        super().add_input(link)
        self.memories[link] = False
        self.false_counts += 1

    def recieve_pulse(self, pulse, name):
        old = self.memories[name]

        if not old and pulse:
            self.false_counts -= 1
        elif old and not pulse:
            self.false_counts += 1

        self.memories[name] = pulse

        if self.false_counts == 0:
            self.pulse_links(False)
        else:
            self.pulse_links(True)

    @property
    def state(self):
        return tuple(self.memories.values())

    @state.setter
    def state(self, value):
        pass


class Broadcast(Module):
    def recieve_pulse(self, pulse, name):
        self.pulse_links(pulse)


def add_modules(names, links):
    for i, name in enumerate(names):
        match name[0]:
            case "b":
                module = Broadcast(name)
            case "%":
                names[i] = name[1:]
                module = FlipFlops(names[i])
            case "&":
                names[i] = name[1:]
                module = Conjuction(names[i])
        modules[names[i]] = module

    for i, name in enumerate(names):
        modules[name].add_links(links[i])
        for link in links[i]:
            if link not in modules:
                modules[link] = Module(link)
            modules[link].add_input(name)
    return modules


def process(antipenultimates=None):
    while pulse_sequence:
        link, pulse, name = pulse_sequence.popleft()
        modules[link].recieve_pulse(pulse, name)

        if antipenultimates:
            if pulse and name in antipenultimates:
                return name


def state():
    state = []
    for module in modules:
        state.append(modules[module].state)
    return tuple(state)
