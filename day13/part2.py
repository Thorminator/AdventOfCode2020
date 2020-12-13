def parse_input(file_name):
    with open(file_name) as f:
        input_split = f.read().split("\n")
        return int(input_split[0]), [int(s) if s != "x" else None for s in input_split[1].split(",")]

_, buses = parse_input("example1.txt")
values = [bus + i for i, bus in enumerate(buses) if bus is not None]