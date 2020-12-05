import re

with open("input.txt") as f:
    print(max([int(re.sub(r"[FL]", "0", re.sub(r"[BR]", "1", s)), 2) for s in f.readlines()]))
