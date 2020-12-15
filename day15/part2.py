def parse_input(file_name):
    with open(file_name) as f:
        return f.read().split(",")


spoken = {int(n): turn + 1 for turn, n in enumerate(parse_input("input.txt"))}
current = list(spoken.keys())[-1]
for i in range(len(spoken), 30000000):
    spoken[current], current = (i, i - spoken[current]) if current in spoken else (i, 0)
print(current)
