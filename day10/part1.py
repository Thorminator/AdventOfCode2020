def parse_input(file_name):
    with open(file_name) as f:
        return [int(line) for line in f.read().split("\n")]


numbers = sorted(parse_input("input.txt"))
diffs = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 1
         }
current = 0
for n in numbers:
    diff = n - current
    diffs[str(diff)] += 1
    current = n
print(diffs["1"] * diffs["3"])
