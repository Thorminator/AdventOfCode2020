import re


def parse(s):
    return int(re.sub(r"[FL]", "0", re.sub(r"[BR]", "1", s)), 2)


with open("input.txt") as f:
    ids = [parse(s[:7]) * 8 + parse(s[7:]) for s in f.readlines()]
    for i in range(min(ids), max(ids)):
        if i not in ids:
            print(i)
