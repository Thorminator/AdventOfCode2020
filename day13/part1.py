import math

def parse_input(file_name):
    with open(file_name) as f:
        input_split = f.read().split("\n")
        return int(input_split[0]), [int(s) for s in input_split[1].split(",") if s != "x"]

timestamp, buses = parse_input("input.txt")
possible_departures = [math.ceil(timestamp / bus) * bus for bus in buses]
earliest_departure_index = min(range(len(possible_departures)), key=possible_departures.__getitem__)
print(buses[earliest_departure_index] * (possible_departures[earliest_departure_index] - timestamp))
