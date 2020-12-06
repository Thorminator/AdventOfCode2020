
with open("input.txt") as f:
    groups = f.read().split("\n\n")

print(sum(len(set(s.replace("\n", ""))) for s in groups))
