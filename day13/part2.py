import math

def parse_input(file_name):
    with open(file_name) as f:
        input_split = f.read().split("\n")
        return int(input_split[0]), [int(s) if s != "x" else None for s in input_split[1].split(",")]


_, buses = parse_input("input.txt")
matched_buses = []
t = buses[0]


def match_bus(bus, index, iteration_value, current_t):
    t = current_t
    if t == 0:
        t += iteration_value
    while True:
        if (t + index) % bus == 0:
            return t
        else:
            t += iteration_value


for i, bus in enumerate(buses):
    if bus is None:
        continue

    iteration_value = math.lcm(*matched_buses) if len(matched_buses) > 0 else bus
    t = match_bus(bus, i, iteration_value, t)
    matched_buses.append(bus)
print(t)
